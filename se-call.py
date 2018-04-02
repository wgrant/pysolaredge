#!/usr/bin/python3

import codecs
import sys

import solaredge.session


device_id = int(sys.argv[1], 16)
message_type = int(sys.argv[2], 16)
message_data = codecs.decode(sys.argv[3], 'hex')

s = solaredge.session.Session(('localhost', 22223), 0xfffffffd)
resp = s.call(device_id, message_type, message_data)
print(
    "0x{:04x}: {}".format(
        resp.type,
        codecs.encode(resp.data, 'hex').decode('ascii')))
print("        {}".format("".join(
    (c if c.isprintable() else '\ufffd')
    for c in resp.data.decode('ascii', errors='replace'))))
