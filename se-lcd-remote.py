#!/usr/bin/python3

import enum
import select
import struct
import sys

import solaredge.session
from solaredge.devices.polestar import PolestarMessageType


class PortiaButton(enum.Enum):
    LCD_DISPLAY = 0
    ENTER = 5
    DOWN = 10
    UP = 15
    ESC = 20


class PortiaButtonDuration(enum.Enum):
    SHORT = 1
    LONG = 3
    LONG_NOT_RELEASED = 4


device_id = int(sys.argv[1], 16)
s = solaredge.session.Session(('localhost', 22223), 0xfffffffd)


def print_lcd():
    resp = s.call(
        device_id, PolestarMessageType.CMD_POLESTAR_READ_LCD.value, b'')
    print(resp.data[0:20].decode('ascii'))
    print(resp.data[20:40].decode('ascii'))
    print(resp.data[40:60].decode('ascii'))
    print(resp.data[60:80].decode('ascii'))


while True:
    print_lcd()
    sys.stdout.write('> ')
    sys.stdout.flush()

    i, _, _ = select.select([sys.stdin], [], [], 1)
    if not i:
        sys.stdout.write('\033[4F')
        continue

    button = sys.stdin.readline().strip()
    if not button:
        continue

    if 'u' in button:
        encoded = PortiaButton.UP.value
    elif 'd' in button:
        encoded = PortiaButton.DOWN.value
    elif 'e' in button:
        encoded = PortiaButton.ENTER.value
    elif 'x' in button:
        encoded = PortiaButton.ESC.value
    else:
        encoded = PortiaButton.LCD_DISPLAY.value

    if 'l' in button:
        encoded |= PortiaButtonDuration.LONG.value
    elif 'l' in button:
        encoded |= PortiaButtonDuration.LONG_NOT_RELEASED.value
    else:
        encoded |= PortiaButtonDuration.SHORT.value

    s.call(
        device_id,
        PolestarMessageType.CMD_POLESTAR_SIMULATE_BUTTON_PRESSING.value,
        struct.pack('<B', encoded))
