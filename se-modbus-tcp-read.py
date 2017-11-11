#!/usr/bin/env python3

import datetime
import json
import socket
import struct
import sys
import time

host, port = sys.argv[1].split(':')

socket.setdefaulttimeout(10)

s = socket.socket()
s.connect((host, int(port)))


def modbus_read_holding(s, base, count):
    assert base >= 40001
    s.send(struct.pack('>HHHBBHH', 1, 0, 6, 0, 3, base - 40001, count))
    r = s.recv(1024)
    txn, proto, length, unit, function, n = struct.unpack('>HHHBBB', r[:9])
    assert txn == 1
    assert proto == 0
    assert unit == 0
    assert function == 3
    assert length == n + 3
    return r[9:9 + n]


res = modbus_read_holding(s, 40001, 69)
(C_SunSpec_ID, C_SunSpec_DID, C_SunSpec_Length, C_Manufacturer, C_Model,
 _, C_Version, C_SerialNumber, C_DeviceAddress) = struct.unpack(
     '>LHH32s32s16s16s32sH', res)

C_Manufacturer = C_Manufacturer.partition(b'\0')[0].decode('UTF-8')
C_Model = C_Model.partition(b'\0')[0].decode('UTF-8')
C_Version = C_Version.partition(b'\0')[0].decode('UTF-8')
C_SerialNumber = C_SerialNumber.partition(b'\0')[0].decode('UTF-8')

while True:
    res = modbus_read_holding(s, 40072, 50)

    (I_AC_Current, I_AC_CurrentA, I_AC_CurrentB, I_AC_CurrentC,
     I_AC_Current_SF, I_AC_VoltageAB, I_AC_VoltageBC, I_AC_VoltageCA,
     I_AC_VoltageAN, I_AC_VoltageBN, I_AC_VoltageCN, I_AC_Voltage_SF,
     I_AC_Power, I_AC_Power_SF, I_AC_Frequency, I_AC_Frequency_SF,
     I_AC_VA, I_AC_VA_SF, I_AC_VAR, I_AC_VAR_SF, I_AC_PF, I_AC_PF_SF,
     I_AC_Energy_WH, I_AC_Energy_WH_SF, I_DC_Current, I_DC_Current_SF,
     I_DC_Voltage, I_DC_Voltage_SF, I_DC_Power, I_DC_Power_SF, _,
     I_Temp_Sink, _, _, I_Temp_SF, I_Status, I_Status_Vendor, _, _,
     I_Event_1_Vendor, _, _, I_Event_4_Vendor) = struct.unpack(
         '>HHHHhHHHHHHhhhHhhhhhhhLHHhHhhhhhhhhHHLLLLLL', res)
    d = {
        "C_Manufacturer": C_Manufacturer, "C_Model": C_Model,
        "C_Version": C_Version, "C_SerialNumber": C_SerialNumber,
        "C_DeviceAddress": C_DeviceAddress,
        "I_AC_Current": I_AC_Current, "I_AC_CurrentA": I_AC_CurrentA,
        "I_AC_CurrentB": I_AC_CurrentB, "I_AC_CurrentC": I_AC_CurrentC,
        "I_AC_Current_SF": I_AC_Current_SF,
        "I_AC_VoltageAB": I_AC_VoltageAB, "I_AC_VoltageBC": I_AC_VoltageBC,
        "I_AC_VoltageCA": I_AC_VoltageCA, "I_AC_VoltageAN": I_AC_VoltageAN,
        "I_AC_VoltageBN": I_AC_VoltageBN, "I_AC_VoltageCN": I_AC_VoltageCN,
        "I_AC_Voltage_SF": I_AC_Voltage_SF,
        "I_AC_Power": I_AC_Power, "I_AC_Power_SF": I_AC_Power_SF,
        "I_AC_Frequency": I_AC_Frequency,
        "I_AC_Frequency_SF": I_AC_Frequency_SF,
        "I_AC_VA": I_AC_VA, "I_AC_VA_SF": I_AC_VA_SF,
        "I_AC_VAR": I_AC_VAR, "I_AC_VAR_SF": I_AC_VAR_SF,
        "I_AC_PF": I_AC_PF, "I_AC_PF_SF": I_AC_PF_SF,
        "I_AC_Energy_WH": I_AC_Energy_WH,
        "I_AC_Energy_WH_SF": I_AC_Energy_WH_SF,
        "I_DC_Current": I_DC_Current, "I_DC_Current_SF": I_DC_Current_SF,
        "I_DC_Voltage": I_DC_Voltage, "I_DC_Voltage_SF": I_DC_Voltage_SF,
        "I_Temp_Sink": I_Temp_Sink, "I_Temp_SF": I_Temp_SF,
        "I_Status": I_Status, "I_Status_Vendor": I_Status_Vendor,
        "I_Event_1_Vendor": I_Event_1_Vendor,
        "I_Event_4_Vendor": I_Event_4_Vendor,
        }
    d['timestamp'] = datetime.datetime.utcnow().isoformat()
    print(json.dumps(d))
    sys.stdout.flush()

    time.sleep(10)
