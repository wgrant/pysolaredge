import codecs
import enum
import struct


class ParameterType(enum.Enum):
    UINT = 0
    FLOAT = 1
    INT = 2
    STRING = 3


def decode_parameter_ids(raw):
    param_ids = []
    while raw:
        assert len(raw) >= 2
        param_id, = struct.unpack('<H', raw[:2])
        param_ids.append(param_id)
        raw = raw[2:]
    return param_ids


def decode_parameters(raw):
    params = []
    while raw:
        assert len(raw) >= 6
        param_type = ParameterType(struct.unpack('<H', raw[4:6])[0])
        if param_type == ParameterType.UINT:
            value, = struct.unpack('<L', raw[:4])
            raw = raw[6:]
        elif param_type == ParameterType.FLOAT:
            value, = struct.unpack('<f', raw[:4])
            raw = raw[6:]
        elif param_type == ParameterType.INT:
            value, = struct.unpack('<l', raw[:4])
            raw = raw[6:]
        elif param_type == ParameterType.STRING:
            # The int value is usually zero, but not always. Ignore for now.
            value, sep, raw = raw[6:].partition(b'\x00')
            assert sep == b'\x00'
        else:
            raise AssertionError("Unknown parameter type")
        params.append(value)
    return params
