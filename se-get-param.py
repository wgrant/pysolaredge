#!/usr/bin/python3

import sys

from solaredge.commands import GenericMessageType
import solaredge.params
import solaredge.session

device_id = int(sys.argv[1], 16)
param_ids = [int(arg, 16) for arg in sys.argv[2:]]

s = solaredge.session.Session(('localhost', 22223), 0xfffffffd)
resp = s.call(
    device_id, GenericMessageType.CMD_PARAMS_GET_SINGLE.value,
    solaredge.params.encode_parameter_ids(param_ids))
print("0x{:x}: {}".format(
    resp.type, solaredge.params.decode_parameters(resp.data)))
