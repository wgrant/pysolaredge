#!/usr/bin/env python3

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
    print(msg.format(type_enum=solaredge.commands.MessageType))
    try:
        decoder = solaredge.commands.MESSAGE_DECODERS[
            solaredge.commands.MessageType(msg.type)]
    except (KeyError, ValueError):
        pass
    else:
        print('  %r' % (decoder(msg.data),))
    c = tail
