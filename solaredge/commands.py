import enum

import solaredge.devices.polestar
import solaredge.devices.venus
import solaredge.params
import solaredge.telemetry


class GenericMessageType(enum.Enum):
    CMD_PARAMS_GET_SINGLE = 0x0012
    RESP_ACK = 0x0080
    RESP_NACK = 0x0081
    RESP_PARAMS_SINGLE = 0x0090

    CMD_SERVER_POST_DATA = 0x0500
    CMD_SERVER_GET_GMT = 0x0501
    RESP_SERVER_GMT = 0x0580


def get_parameter_id(msg, param_id):
    if ((not msg.addr_from & 0x80000000 and msg.addr_from & 0x00800000)
            or (not msg.addr_to & 0x80000000 and msg.addr_to & 0x00800000)):
        # It's an inverter. Assume Venus for now.
        param_enum = solaredge.devices.venus.VenusParameters
    elif not msg.addr_from & 0x80000000 or not msg.addr_to & 0x80000000:
        # It's probably a Polestar.
        param_enum = solaredge.devices.polestar.PolestarParameters
    else:
        param_enum = None
    if param_enum is not None:
        try:
            return param_enum(param_id)
        except ValueError:
            pass
    return param_id


def decode_param_ids_message(data):
    return [
        get_parameter_id(msg, param_id)
        for param_id in solaredge.params.decode_parameter_ids(msg.data)]


TYPE_CLASSES = []


def register_enum(cls):
    if cls not in TYPE_CLASSES:
        TYPE_CLASSES.append(cls)


MESSAGE_DECODERS = {
    GenericMessageType.CMD_PARAMS_GET_SINGLE: decode_param_ids_message,
    GenericMessageType.RESP_PARAMS_SINGLE:
        lambda msg: solaredge.params.decode_parameters(msg.data),
    GenericMessageType.CMD_SERVER_POST_DATA:
        lambda msg: solaredge.telemetry.decode_telems(msg.data),
    }


def register_decoders(decoders):
    for type, decoder in decoders.items():
        if type in MESSAGE_DECODERS:
            raise Exception("Duplicate decoder for %s" % type)
        MESSAGE_DECODERS[type] = decoder


class UnknownCommand(Exception):
    pass


def decode_type(type_id):
    for cls in TYPE_CLASSES:
        try:
            return cls(type_id)
        except ValueError:
            continue


def decode_message(msg):
    type = decode_type(msg.type) or msg.type
    decoder = MESSAGE_DECODERS.get(type)
    data = decoder(msg) if decoder else msg.data
    return type, data


register_enum(GenericMessageType)
register_enum(solaredge.devices.polestar.PolestarMessageType)
register_enum(solaredge.devices.venus.VenusMessageType)
register_decoders(solaredge.devices.polestar.MESSAGE_DECODERS)
