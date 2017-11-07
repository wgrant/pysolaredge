#!/usr/bin/env python3

import codecs
import logging
import sys

import solaredge.commands
import solaredge.proto

def get_message_type(msg):
    if ((not msg.addr_from & 0x80000000 and msg.addr_from & 0x00800000)
            or (not msg.addr_to & 0x80000000 and msg.addr_to & 0x00800000)):
        # It's an inverter. Assume Venus for now.
        mt_enums = (
            solaredge.commands.VenusMessageType,
            solaredge.commands.GenericMessageType,
            )
    elif not msg.addr_from & 0x80000000 or not msg.addr_to & 0x80000000:
        # It's probably a Polestar.
        mt_enums = (
            solaredge.commands.PolestarMessageType,
            solaredge.commands.GenericMessageType,
            )
    elif msg.addr_from == 0xffffffff or msg.addr_to == 0xffffffff:
        mt_enums = (
            solaredge.commands.VenusMessageType,
            solaredge.commands.PolestarMessageType,
            solaredge.commands.GenericMessageType,
            )
    else:
        mt_enums = (solaredge.commands.GenericMessageType,)
    for mt_enum in mt_enums:
        try:
            return mt_enum(msg.type)
        except ValueError:
            pass
    return msg.type


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
    msg_type = get_message_type(msg)
    try:
        decoder = solaredge.commands.MESSAGE_DECODERS[msg_type]
    except (KeyError, ValueError):
        decoded = codecs.encode(msg.data, 'hex').decode('ascii')
    else:
        decoded = decoder(msg.data)
    print('  %s: %s' % (msg_type, decoded))
    c = tail
