import codecs
import datetime
import enum
import struct


# The inverter sends 0xff7fffff as a float to indicate it has no data.
NULL_FLOAT, = struct.unpack('<f', b'\xff\xff\x7f\xff')


class TelemRecordType(enum.Enum):
    PANEL = 0x0000
    STRING = 0x0001
    CLUSTER = 0x0002
    INVERTER_1PHASE = 0x0010
    INVERTER_3PHASE = 0x0011
    COMBI_STRING = 0x0012
    COMBI = 0x0013
    UNIFIED_COMBI_STRING = 0x0014
    UNIFIED_COMBI = 0x0015
    xx_VEGA = 0x0016
    xx_DAILY = 0x0017
    xx_INVDAILY = 0x0018
    xx_SENSOR = 0x0020
    xx_METER = 0x0022
    xx_STORAGEDAILY = 0x0030
    xx_STORAGEDAILY2 = 0x0040
    xx_UNK = 0x0041
    xx_METERDAILY = 0x0042
    xx_PANEL_NEW = 0x0080
    xx_INVERTER_1PHASE_NEW = 0x0090
    xx_INVERTER_3PHASE_NEW = 0x0091
    VENUS = 0x0200
    POLESTAR = 0x300
    xx_POLESTAR_1 = 0x301
    xx_POLESTAR_2 = 0x302
    SUNTRACER = 0x400
    JUPITER = 0x800
    VEGA = 0xa00


class InverterMode(enum.Enum):
    OFF = 1
    SLEEPING = 2
    STARTING = 3
    MPPT = 4 # "Production"
    THROTTLED = 5 # "Power Limitation"
    STANDBY = 8


def decode_telem(dev_type, telem_data):
    if dev_type == TelemRecordType.xx_PANEL_NEW:
        timestamp, uptime, power_attrs, energy, temp = struct.unpack(
            '<LHLHB', telem_data)
        temp *= 2.0
        vdc_in = 0.125 * (power_attrs & 0x000003ff)
        vdc_out = 0.125 * ((power_attrs & 0x000ffc00) >> 10)
        i_in = 0.00625 * ((power_attrs & 0xfff00000) >> 20)
        energy = 0.25 * energy  # Energy produced since optimiser boot.
        return {
            "timestamp": datetime.datetime.utcfromtimestamp(timestamp),
            "uptime": uptime, "vdc_in": vdc_in, "i_in": i_in,
            "vdc_out": vdc_out, "energy": energy, "temp": temp,
            }
    elif dev_type == TelemRecordType.INVERTER_1PHASE:
        (timestamp, uptime, interval, temp, e_ac, e_ac_interval, v_ac,
         i_ac, f_ac, e_dc, e_dc_interval, v_dc, i_dc, e_ac_total, i_rcd,
         unk1, cos_phi, inverter_mode, isolation, power_limit, i_ac_dc_maybe,
         unk2, unk3, p_ac, p_ac_apparent, p_ac_reactive, power_limit_unk1,
         power_limit_2, power_limit_unk2, e_ac_total_int) = [
             (v if v != NULL_FLOAT else None) for v in
             struct.unpack(
                 '<LLLffffffffffffffLfffffffffffL', telem_data[:120])]
        # XXX: Unknown 56-byte tail, too.

        # I don't know what i_ac_dc is, since it's too low to be
        # conversion overhead, but it's "I AC/DC [A]" in the web UI.

        # power_limit and power_limit_2 seem identical, at least when
        # manually configured.

        try:
            inverter_mode = InverterMode(inverter_mode)
        except ValueError:
            pass

        # e_dc, e_dc_interval, i_dc are hardcoded to 0xff7fffff in the
        # firmware.
        return {
            "timestamp": datetime.datetime.utcfromtimestamp(timestamp),
            "uptime": uptime, "interval": interval, "e_ac": e_ac,
            "e_ac_interval": e_ac_interval, "v_ac": v_ac, "i_ac": i_ac,
            "f_ac": f_ac, "v_dc": v_dc, "e_ac_total": e_ac_total,
            "i_rcd": i_rcd, "cos_phi": cos_phi,
            "inverter_mode": inverter_mode, "isolation": isolation,
            "i_ac_dc": i_ac_dc_maybe, "power_limit": power_limit,
            "p_ac": p_ac, "p_ac_apparent": p_ac_apparent,
            "p_ac_reactive": p_ac_reactive, "power_limit_2": power_limit_2,
            "power_limit_unk1": power_limit_unk1,
            "power_limit_unk2": power_limit_unk2,
            "e_ac_total_int": e_ac_total_int, "unk1": unk1, "unk2": unk2,
            "unk3": unk3}

    # XXX: We're just assuming that each record starts with a timestamp.
    timestamp = datetime.datetime.utcfromtimestamp(
        struct.unpack('<L', telem_data[:4])[0])
    return {
        "timestamp": timestamp,
        "unknown": telem_data[4:],
        }


def decode_telems(raw):
    telems = []
    while raw:
        assert len(raw) >= 8
        record_type, dev_id, telem_len = struct.unpack('<HLH', raw[:8])
        try:
            record_type = TelemRecordType(record_type)
        except ValueError:
            pass
        try:
            telem = decode_telem(record_type, raw[8:8 + telem_len])
        except Exception as e:
            telem = '%s: %s' % (
                repr(e), codecs.encode(raw[8:8 + telem_len], 'hex'))
        telems.append((record_type, dev_id, telem))
        raw = raw[8 + telem_len:]
    return telems
