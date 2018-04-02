#!/usr/bin/env python3

import codecs
import logging
import sys

import solaredge.commands
import solaredge.proto


with open(sys.argv[1], 'rb') as f:
    c = f.read()

while solaredge.proto.MAGIC in c:
    c = c[c.index(solaredge.proto.MAGIC):]
    try:
        msg, tail = solaredge.proto.decode_message_with_tail(c)
    except Exception as e:
        logging.exception("Failed.")
        msg = None
        c = c[1:]
        continue
    print(repr(msg))

    type, payload = solaredge.commands.decode_message(msg)

    if isinstance(type, int):
        type = "0x{:04x}".format(type)

    if isinstance(payload, bytes):
        payload = "".join(
            (c if c.isprintable() else '\ufffd')
            for c in msg.data.decode('ascii', errors='replace'))

    print("{}: {}".format(type, payload))

    c = tail
