#!/usr/bin/python3

import codecs
import sys

import solaredge.commands
import solaredge.session


device_id = int(sys.argv[1], 16)
message_type = int(sys.argv[2], 16)
if len(sys.argv) >= 4:
    message_data = codecs.decode(sys.argv[3], 'hex')
else:
    message_data = b''

s = solaredge.session.Session(('localhost', 22223), 0xfffffffd)
resp = s.call(device_id, message_type, message_data)
print(
    "0x{:04x}: {}".format(
        resp.type,
        codecs.encode(resp.data, 'hex').decode('ascii')))

type, payload = solaredge.commands.decode_message(resp)

if isinstance(type, int):
    type = "0x{:04x}".format(type)

if isinstance(payload, bytes):
    payload = "".join(
        (c if c.isprintable() else '\ufffd')
        for c in resp.data.decode('ascii', errors='replace'))

print("{}: {}".format(type, payload))
