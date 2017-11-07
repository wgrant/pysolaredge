import enum

import solaredge.params


class GenericMessageType(enum.Enum):
    CMD_PARAMS_GET_SINGLE = 0x0012
    RESP_ACK = 0x0080
    RESP_NACK = 0x0081
    RESP_PARAMS_SINGLE = 0x0090

    CMD_SERVER_POST_DATA = 0x0500
    CMD_SERVER_GET_GMT = 0x0501
    RESP_SERVER_GMT = 0x0580


class PolestarMessageType(enum.Enum):
    CMD_POLESTAR_MAC_ADDR_GET = 0x0306
    CMD_POLESTAR_IP_ADDR_GET = 0x0307
    CMD_POLESTAR_SEND_PING = 0x030c
    CMD_POLESTAR_CONFTOOL_START = 0x030e
    CMD_POLESTAR_ETHERNET_STAT = 0x030f
    CMD_POLESTAR_GET_POK_STATUS = 0x031c
    CMD_POLESTAR_ZB_PRESENT_STATUS = 0x031e
    CMD_POLESTAR_GET_S_OK_STATUS = 0x0321
    CMD_POLESTAR_GET_ENERGY_STATISTICS_STATUS = 0x0322
    CMD_POLESTAR_BLOCK_SERVER_CONTROL = 0x0329
    CMD_POLESTAR_GET_SERVER_CONTROL_STATUS = 0x032a
    RESP_POLESTAR_MAC_ADDR_GET = 0x0381
    RESP_POLESTAR_IP_ADDR_GET = 0x0382
    RESP_POLESTAR_SEND_PING = 0x0383
    RESP_POLESTAR_ETHERNET_STAT = 0x0384
    RESP_POLESTAR_GET_POK_STATUS = 0x0388
    RESP_POLESTAR_GET_S_OK_STATUS = 0x038c
    RESP_POLESTAR_GET_ENERGY_STATISTICS_STATUS = 0x038d
    RESP_POLESTAR_GET_SERVER_CONTROL_STATUS = 0x0392


class VenusMessageType(enum.Enum):
    CMD_VENUSMNGR_GET_SYS_STATUS = 0x0205
    CMD_VENUSMNGR_KA_DATA_SEND = 0x0218
    RESP_VENUSMNGR_GET_SYS_STATUS = 0x0283


def get_parameter_id(msg, param_id):
    if ((not msg.addr_from & 0x80000000 and msg.addr_from & 0x00800000)
            or (not msg.addr_to & 0x80000000 and msg.addr_to & 0x00800000)):
        # It's an inverter. Assume Venus for now.
        param_enum = solaredge.params.VenusParameters
    elif not msg.addr_from & 0x80000000 or not msg.addr_to & 0x80000000:
        # It's probably a Polestar.
        param_enum = solaredge.params.PolestarParameters
    else:
        param_enum = None
    if param_enum is not None:
        try:
            return param_enum(param_id)
        except ValueError:
            pass
    return param_id


def decode_param_ids_message(msg):
    return [
        get_parameter_id(msg, param_id)
        for param_id in solaredge.params.decode_parameter_ids(msg.data)]


MESSAGE_DECODERS = {
    GenericMessageType.CMD_PARAMS_GET_SINGLE: decode_param_ids_message,
    GenericMessageType.RESP_PARAMS_SINGLE:
        lambda msg: solaredge.params.decode_parameters(msg.data),
    }
