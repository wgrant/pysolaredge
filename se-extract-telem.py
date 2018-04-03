#!/usr/bin/python3

import base64
import json
import sys

import solaredge.commands
import solaredge.telemetry

f = open(sys.argv[1], 'rt')

for line in f:
    # Ignore incomplete final lines.
    if not line.endswith('\n'):
        break
    msg = json.loads(line.strip())
    if (msg['type'] !=
            solaredge.commands.GenericMessageType.CMD_SERVER_POST_DATA.value):
        continue
    telems = solaredge.telemetry.decode_telems(base64.b64decode(msg['data']))
    for ttype, tdev, tdata in telems:
        ts = tdata.pop('timestamp')
        print("{} {:16} {:08x}: {}".format(
              ts.isoformat(),
              ttype.name if not isinstance(ttype, int)
              else "{:04X}".format(ttype),
              tdev,
              " ".join("{}={}".format(k, v) for k, v in tdata.items())))
