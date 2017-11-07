import enum


class PolestarParameters(enum.Enum):
    ID = 0x0000
    VER_MAJOR = 0x0001
    VER_MINOR = 0x0002
    VENUS_ADDR_MASK = 0x0003
    INV_MODEL_NUMBER = 0x0004
    INV_SERIAL_NUMBER = 0x0005
    ENABLE_ZB = 0x0006
    ENABLE_RS485 = 0x0007
    ENABLE_TCP = 0x0008
    ENABLE_DHCP = 0x0009
    POWER_CAL_FACTOR = 0x000a
    MAC_OUI_ADDRESS = 0x000b
    MY_IP = 0x000c
    MY_SUBNETMASK_IP = 0x000d
    MY_GATEWAY_IP = 0x000e
    MY_DNS_IP = 0x000f
    SERVER_IP1 = 0x0010
    SERVER_IP2 = 0x0011
    SERVER_IP3 = 0x0012
    TCP_SERVER_PORT = 0x0013
    TCP_CONNECTION_TIMEOUT_MSEC = 0x0014
    ETH_CONNECTED = 0x0015
    WATCHDOG_ENABLE = 0x0016
    RTC_ENABLE_UPDATE = 0x0017
    RTC_GMT_OFFSET = 0x0018
    STREAM_SERVER = 0x0019
    STREAM_IO = 0x001a
    ENABLE_IO = 0x001b
    SERVER_RESP_TIMEOUT = 0x001c
    SERVER_FLUSH_TIMEOUT = 0x001d
    MODULES_LIST_TIMEOUT = 0x001e
    CTRL_PNL_ENABLE = 0x001f
    CTRL_PNL_ENABLE_BACKLIGHT_OFF = 0x0020
    CTRL_PNL_BACKLIGHT_ON_SEC = 0x0021
    CTRL_PNL_TELEM_BACKLIGHT_ON_MIN = 0x0022
    CTRL_PNL_FILTER_TIME = 0x0023
    CTRL_PNL_PREV_FILTER_WEIGHT = 0x0024
    CTRL_PNL_UPDATE_PRINT_MSEC = 0x0025
    OPMODE_SHTDN_SFTY_V = 0x0026
    OPMODE_SHTDN_SFTY_T = 0x0027
    SETUP_PASSWORD = 0x0028
    SETUP_MENU_QUIT_TIME_MSEC = 0x0029
    RESERVED1 = 0x002a
    SETUP_COUNTRY_SHORT = 0x002b
    SETUP_LANGUAGE = 0x002c
    SETUP_TEMPERATURE_DISPALY = 0x002d
    SETUP_COUNTRY_NORTH_AMERICA_ZONE = 0x002e
    SETUP_COUNTRY_EUROPE_ZONE = 0x002f
    SETUP_COUNTRY_APAC_ZONE = 0x0030
    SETUP_COUNTRY_ALL_ZONES = 0x0031
    ZIGBEE_MASTER = 0x0032
    ZIGBEE_PAN_ID = 0x0033
    ZIGBEE_SCAN_CHANNELS_MASK = 0x0034
    ZIGBEE_JITTER_TIME_MSEC = 0x0035
    RS485_MASTER = 0x0036
    RS485_SLV_DETECT_PERIOD = 0x0037
    RS485_SLV_DETECT_LOOPS = 0x0038
    RS485_GRANT_SLOT_MSEC = 0x0039
    NUM_OF_PS_SLV = 0x003a
    PS_SLV_ID0 = 0x003b
    PS_SLV_ID1 = 0x003c
    PS_SLV_ID2 = 0x003d
    PS_SLV_ID3 = 0x003e
    PS_SLV_ID4 = 0x003f
    PS_SLV_ID5 = 0x0040
    PS_SLV_ID6 = 0x0041
    PS_SLV_ID7 = 0x0042
    PS_SLV_ID8 = 0x0043
    PS_SLV_ID9 = 0x0044
    PS_SLV_ID10 = 0x0045
    PS_SLV_ID11 = 0x0046
    PS_SLV_ID12 = 0x0047
    PS_SLV_ID13 = 0x0048
    PS_SLV_ID14 = 0x0049
    PS_SLV_ID15 = 0x004a
    PS_SLV_ID16 = 0x004b
    PS_SLV_ID17 = 0x004c
    PS_SLV_ID18 = 0x004d
    PS_SLV_ID19 = 0x004e
    PS_SLV_ID20 = 0x004f
    PS_SLV_ID21 = 0x0050
    PS_SLV_ID22 = 0x0051
    PS_SLV_ID23 = 0x0052
    PS_SLV_ID24 = 0x0053
    PS_SLV_ID25 = 0x0054
    PS_SLV_ID26 = 0x0055
    PS_SLV_ID27 = 0x0056
    PS_SLV_ID28 = 0x0057
    PS_SLV_ID29 = 0x0058
    PS_SLV_ID30 = 0x0059
    PS_SLV_ID31 = 0x005a
    PS_SLV_ID32 = 0x005b
    PS_SLV_ID33 = 0x005c
    PS_SLV_ID34 = 0x005d
    PS_SLV_ID35 = 0x005e
    PS_SLV_ID36 = 0x005f
    PS_SLV_ID37 = 0x0060
    PS_SLV_ID38 = 0x0061
    PS_SLV_ID39 = 0x0062
    PS_SLV_ID40 = 0x0063
    PS_SLV_ID41 = 0x0064
    PS_SLV_ID42 = 0x0065
    PS_SLV_ID43 = 0x0066
    PS_SLV_ID44 = 0x0067
    PS_SLV_ID45 = 0x0068
    PS_SLV_ID46 = 0x0069
    PS_SLV_ID47 = 0x006a
    PS_SLV_ID48 = 0x006b
    PS_SLV_ID49 = 0x006c
    PS_SLV_ID50 = 0x006d
    PS_SLV_ID51 = 0x006e
    PS_SLV_ID52 = 0x006f
    PS_SLV_ID53 = 0x0070
    PS_SLV_ID54 = 0x0071
    PS_SLV_ID55 = 0x0072
    PS_SLV_ID56 = 0x0073
    PS_SLV_ID57 = 0x0074
    PS_SLV_ID58 = 0x0075
    PS_SLV_ID59 = 0x0076
    PS_SLV_ID60 = 0x0077
    PS_SLV_ID61 = 0x0078
    PS_SLV_ID62 = 0x0079
    PS_SLV_ID63 = 0x007a
    PS_SLV_ID64 = 0x007b
    PS_SLV_ID65 = 0x007c
    PS_SLV_ID66 = 0x007d
    PS_SLV_ID67 = 0x007e
    PS_SLV_ID68 = 0x007f
    PS_SLV_ID69 = 0x0080
    PS_SLV_ID70 = 0x0081
    PS_SLV_ID71 = 0x0082
    PS_SLV_ID72 = 0x0083
    PS_SLV_ID73 = 0x0084
    PS_SLV_ID74 = 0x0085
    PS_SLV_ID75 = 0x0086
    PS_SLV_ID76 = 0x0087
    PS_SLV_ID77 = 0x0088
    PS_SLV_ID78 = 0x0089
    PS_SLV_ID79 = 0x008a
    PS_SLV_ID80 = 0x008b
    PS_SLV_ID81 = 0x008c
    PS_SLV_ID82 = 0x008d
    PS_SLV_ID83 = 0x008e
    PS_SLV_ID84 = 0x008f
    PS_SLV_ID85 = 0x0090
    PS_SLV_ID86 = 0x0091
    PS_SLV_ID87 = 0x0092
    PS_SLV_ID88 = 0x0093
    PS_SLV_ID89 = 0x0094
    PS_SLV_ID90 = 0x0095
    PS_SLV_ID91 = 0x0096
    PS_SLV_ID92 = 0x0097
    PS_SLV_ID93 = 0x0098
    PS_SLV_ID94 = 0x0099
    PS_SLV_ID95 = 0x009a
    PS_SLV_ID96 = 0x009b
    PS_SLV_ID97 = 0x009c
    PS_SLV_ID98 = 0x009d
    PS_SLV_ID99 = 0x009e
    PS_SLV_ID100 = 0x009f
    PS_SLV_ID101 = 0x00a0
    PS_SLV_ID102 = 0x00a1
    PS_SLV_ID103 = 0x00a2
    PS_SLV_ID104 = 0x00a3
    PS_SLV_ID105 = 0x00a4
    PS_SLV_ID106 = 0x00a5
    PS_SLV_ID107 = 0x00a6
    PS_SLV_ID108 = 0x00a7
    PS_SLV_ID109 = 0x00a8
    PS_SLV_ID110 = 0x00a9
    PS_SLV_ID111 = 0x00aa
    PS_SLV_ID112 = 0x00ab
    PS_SLV_ID113 = 0x00ac
    PS_SLV_ID114 = 0x00ad
    PS_SLV_ID115 = 0x00ae
    PS_SLV_ID116 = 0x00af
    PS_SLV_ID117 = 0x00b0
    PS_SLV_ID118 = 0x00b1
    PS_SLV_ID119 = 0x00b2
    PS_SLV_ID120 = 0x00b3
    PS_SLV_ID121 = 0x00b4
    PS_SLV_ID122 = 0x00b5
    PS_SLV_ID123 = 0x00b6
    PS_SLV_ID124 = 0x00b7
    PS_SLV_ID125 = 0x00b8
    PS_SLV_ID126 = 0x00b9
    PS_SLV_ID127 = 0x00ba
    POWER_BALANCE_SHUTDOWN = 0x00bb
    VERSION_CHECKSUM = 0x00bc
    STREAM_POLESTARS = 0x00bd
    ZB_MASTER_ADDRESS_HIGH = 0x00be
    ZB_MASTER_ADDRESS_LOW = 0x00bf
    SERVER_COM_MODE = 0x00c0
    POLESTAR_MODE = 0x00c1
    ZB_MAX_HOPS = 0x00c2
    ENABLE_GSM = 0x00c3
    GSM_MODEM_TYPE = 0x00c4
    GSM_ACCESS_POINT_NAME = 0x00c5
    GSM_USER_NAME = 0x00c6
    GSM_PASSWORD = 0x00c7
    GSM_NUM_OF_CONN_CMDS = 0x00c8
    GSM_NUM_OF_DISCONN_CMDS = 0x00c9
    GSM_CONN_CMD_1 = 0x00ca
    GSM_CONN_RESP_1 = 0x00cb
    GSM_CONN_CMD_2 = 0x00cc
    GSM_CONN_RESP_2 = 0x00cd
    GSM_CONN_CMD_3 = 0x00ce
    GSM_CONN_RESP_3 = 0x00cf
    GSM_CONN_CMD_4 = 0x00d0
    GSM_CONN_RESP_4 = 0x00d1
    GSM_CONN_CMD_5 = 0x00d2
    GSM_CONN_RESP_5 = 0x00d3
    GSM_CONN_CMD_6 = 0x00d4
    GSM_CONN_RESP_6 = 0x00d5
    GSM_CONN_CMD_7 = 0x00d6
    GSM_CONN_RESP_7 = 0x00d7
    GSM_CONN_CMD_8 = 0x00d8
    GSM_CONN_RESP_8 = 0x00d9
    GSM_CONN_CMD_9 = 0x00da
    GSM_CONN_RESP_9 = 0x00db
    GSM_CONN_CMD_10 = 0x00dc
    GSM_CONN_RESP_10 = 0x00dd
    GSM_CONN_CMD_11 = 0x00de
    GSM_CONN_RESP_11 = 0x00df
    GSM_CONN_CMD_12 = 0x00e0
    GSM_CONN_RESP_12 = 0x00e1
    GSM_CONN_CMD_13 = 0x00e2
    GSM_CONN_RESP_13 = 0x00e3
    GSM_CONN_CMD_14 = 0x00e4
    GSM_CONN_RESP_14 = 0x00e5
    GSM_CONN_CMD_15 = 0x00e6
    GSM_CONN_RESP_15 = 0x00e7
    GSM_CONN_CMD_16 = 0x00e8
    GSM_CONN_RESP1_6 = 0x00e9
    GSM_CONN_CMD_17 = 0x00ea
    GSM_CONN_RESP_17 = 0x00eb
    GSM_CONN_CMD_18 = 0x00ec
    GSM_CONN_RESP_18 = 0x00ed
    GSM_CONN_CMD_19 = 0x00ee
    GSM_CONN_RESP_19 = 0x00ef
    GSM_CONN_CMD_20 = 0x00f0
    GSM_CONN_RESP_20 = 0x00f1
    GSM_DISCONN_CMD_1 = 0x00f2
    GSM_DISCONN_RESP_1 = 0x00f3
    GSM_DISCONN_CMD_2 = 0x00f4
    GSM_DISCONN_RESP_2 = 0x00f5
    GSM_DISCONN_CMD_3 = 0x00f6
    GSM_DISCONN_RESP_3 = 0x00f7
    GSM_DISCONN_CMD_4 = 0x00f8
    GSM_DISCONN_RESP_4 = 0x00f9
    GSM_DISCONN_CMD_5 = 0x00fa
    GSM_DISCONN_RESP_5 = 0x00fb
    GSM_DISCONN_CMD_6 = 0x00fc
    GSM_DISCONN_RESP_6 = 0x00fd
    GSM_DISCONN_CMD_7 = 0x00fe
    GSM_DISCONN_RESP_7 = 0x00ff
    GSM_DISCONN_CMD_8 = 0x0100
    GSM_DISCONN_RESP_8 = 0x0101
    GSM_DISCONN_CMD_9 = 0x0102
    GSM_DISCONN_RESP_9 = 0x0103
    GSM_DISCONN_CMD_10 = 0x0104
    GSM_DISCONN_RESP_10 = 0x0105
    PS_SLV_ID0_ZB_H = 0x0106
    PS_SLV_ID0_ZB_L = 0x0107
    PS_SLV_ID1_ZB_H = 0x0108
    PS_SLV_ID1_ZB_L = 0x0109
    PS_SLV_ID2_ZB_H = 0x010a
    PS_SLV_ID2_ZB_L = 0x010b
    PS_SLV_ID3_ZB_H = 0x010c
    PS_SLV_ID3_ZB_L = 0x010d
    PS_SLV_ID4_ZB_H = 0x010e
    PS_SLV_ID4_ZB_L = 0x010f
    PS_SLV_ID5_ZB_H = 0x0110
    PS_SLV_ID5_ZB_L = 0x0111
    PS_SLV_ID6_ZB_H = 0x0112
    PS_SLV_ID6_ZB_L = 0x0113
    PS_SLV_ID7_ZB_H = 0x0114
    PS_SLV_ID7_ZB_L = 0x0115
    PS_SLV_ID8_ZB_H = 0x0116
    PS_SLV_ID8_ZB_L = 0x0117
    PS_SLV_ID9_ZB_H = 0x0118
    PS_SLV_ID9_ZB_L = 0x0119
    PS_SLV_ID10_ZB_H = 0x011a
    PS_SLV_ID10_ZB_L = 0x011b
    PS_SLV_ID11_ZB_H = 0x011c
    PS_SLV_ID11_ZB_L = 0x011d
    PS_SLV_ID12_ZB_H = 0x011e
    PS_SLV_ID12_ZB_L = 0x011f
    PS_SLV_ID13_ZB_H = 0x0120
    PS_SLV_ID13_ZB_L = 0x0121
    PS_SLV_ID14_ZB_H = 0x0122
    PS_SLV_ID14_ZB_L = 0x0123
    PS_SLV_ID15_ZB_H = 0x0124
    PS_SLV_ID15_ZB_L = 0x0125
    PS_SLV_ID16_ZB_H = 0x0126
    PS_SLV_ID16_ZB_L = 0x0127
    PS_SLV_ID17_ZB_H = 0x0128
    PS_SLV_ID17_ZB_L = 0x0129
    PS_SLV_ID18_ZB_H = 0x012a
    PS_SLV_ID18_ZB_L = 0x012b
    PS_SLV_ID19_ZB_H = 0x012c
    PS_SLV_ID19_ZB_L = 0x012d
    PS_SLV_ID20_ZB_H = 0x012e
    PS_SLV_ID20_ZB_L = 0x012f
    PS_SLV_ID21_ZB_H = 0x0130
    PS_SLV_ID21_ZB_L = 0x0131
    PS_SLV_ID22_ZB_H = 0x0132
    PS_SLV_ID22_ZB_L = 0x0133
    PS_SLV_ID23_ZB_H = 0x0134
    PS_SLV_ID23_ZB_L = 0x0135
    PS_SLV_ID24_ZB_H = 0x0136
    PS_SLV_ID24_ZB_L = 0x0137
    PS_SLV_ID25_ZB_H = 0x0138
    PS_SLV_ID25_ZB_L = 0x0139
    PS_SLV_ID26_ZB_H = 0x013a
    PS_SLV_ID26_ZB_L = 0x013b
    PS_SLV_ID27_ZB_H = 0x013c
    PS_SLV_ID27_ZB_L = 0x013d
    PS_SLV_ID28_ZB_H = 0x013e
    PS_SLV_ID28_ZB_L = 0x013f
    PS_SLV_ID29_ZB_H = 0x0140
    PS_SLV_ID29_ZB_L = 0x0141
    PS_SLV_ID30_ZB_H = 0x0142
    PS_SLV_ID30_ZB_L = 0x0143
    PS_SLV_ID31_ZB_H = 0x0144
    PS_SLV_ID31_ZB_L = 0x0145
    ENABLE_INV_HW_RESET = 0x0146
    JUPITER_TELEMS_PERIOD = 0x0147
    MODBUS_ENABLE = 0x0148
    MODBUS_SLAVE_ID = 0x0149
    RESERVED_5 = 0x014a
    MODBUS_STATUS = 0x014b
    RTC_TIME = 0x014c
    SYSTEM_LOCAL_TIME = 0x014d
    MODBUS_DEVICE_ENABLE = 0x014e
    MODBUS_DEVICE_ID = 0x014f
    MODBUS_DEVICE_PERMISSIONS = 0x0150
    RESERVED_12 = 0x0151
    STATISTIC_ENERGY_DAY = 0x0152
    STATISTIC_ENERGY_MONTH = 0x0153
    STATISTIC_ENERGY_YEAR = 0x0154
    STATISTIC_ENERGY_TOTAL = 0x0155
    STATISTIC_ENERGY_RTC = 0x0156
    RESERVED_18 = 0x0157
    RESERVED_19 = 0x0158
    RESERVED_20 = 0x0159
    TESTER_RESERVED_1 = 0x015a
    TESTER_RESERVED_2 = 0x015b
    MODBUS_IP_ADDRESS = 0x015c
    RESERVED_24 = 0x015d
    RESERVED_25 = 0x015e
    RESERVED_26 = 0x015f
    RESERVED_27 = 0x0160
    RESERVED_28 = 0x0161
    RESERVED_29 = 0x0162
    RESERVED_30 = 0x0163
    SD_CARD_ENABLE = 0x0164
    SD_CARD_MAX_FIFO_VOLUME = 0x0165
    SD_CARD_STATUS = 0x0166
    MODBUS_SLAVE_STREAM = 0x0167
    MODBUS_SLAVE_PROTOCOL_TYPE = 0x0168
    POLESTAR_HW_VERSION = 0x0169
    POWER_REDUCER_TELEM_PERIOD = 0x016a
    POWER_REDUCER_DEBOUNCE_TIME = 0x016b
    POWER_REDUCER_FAILURE_TIME = 0x016c
    POWER_REDUCER_ENABLE = 0x016d
    ZB_SLV_DETECT_PERIOD = 0x016e
    ZB_SLV_DETECT_LOOPS = 0x016f
    ZB_GRANT_SLOT_MSEC = 0x0170
    NUM_OF_MODULES = 0x0171
    NUM_OF_PAIRED_MODULES = 0x0172
    PAIRED_MODULE_0 = 0x0173
    PAIRED_MODULE_1 = 0x0174
    PAIRED_MODULE_2 = 0x0175
    PAIRED_MODULE_3 = 0x0176
    PAIRED_MODULE_4 = 0x0177
    PAIRED_MODULE_5 = 0x0178
    PAIRED_MODULE_6 = 0x0179
    PAIRED_MODULE_7 = 0x017a
    PAIRED_MODULE_8 = 0x017b
    PAIRED_MODULE_9 = 0x017c
    PAIRED_MODULE_10 = 0x017d
    PAIRED_MODULE_11 = 0x017e
    PAIRED_MODULE_12 = 0x017f
    PAIRED_MODULE_13 = 0x0180
    PAIRED_MODULE_14 = 0x0181
    PAIRED_MODULE_15 = 0x0182
    PAIRED_MODULE_16 = 0x0183
    PAIRED_MODULE_17 = 0x0184
    PAIRED_MODULE_18 = 0x0185
    PAIRED_MODULE_19 = 0x0186
    PAIRED_MODULE_20 = 0x0187
    PAIRED_MODULE_21 = 0x0188
    PAIRED_MODULE_22 = 0x0189
    PAIRED_MODULE_23 = 0x018a
    PAIRED_MODULE_24 = 0x018b
    PAIRED_MODULE_25 = 0x018c
    PAIRED_MODULE_26 = 0x018d
    PAIRED_MODULE_27 = 0x018e
    PAIRED_MODULE_28 = 0x018f
    PAIRED_MODULE_29 = 0x0190
    PAIRED_MODULE_30 = 0x0191
    PAIRED_MODULE_31 = 0x0192
    PAIRED_MODULE_32 = 0x0193
    PAIRED_MODULE_33 = 0x0194
    PAIRED_MODULE_34 = 0x0195
    PAIRED_MODULE_35 = 0x0196
    PAIRED_MODULE_36 = 0x0197
    PAIRED_MODULE_37 = 0x0198
    PAIRED_MODULE_38 = 0x0199
    PAIRED_MODULE_39 = 0x019a
    PAIRED_MODULE_40 = 0x019b
    PAIRED_MODULE_41 = 0x019c
    PAIRED_MODULE_42 = 0x019d
    PAIRED_MODULE_43 = 0x019e
    PAIRED_MODULE_44 = 0x019f
    PAIRED_MODULE_45 = 0x01a0
    PAIRED_MODULE_46 = 0x01a1
    PAIRED_MODULE_47 = 0x01a2
    PAIRED_MODULE_48 = 0x01a3
    PAIRED_MODULE_49 = 0x01a4
    PAIRED_MODULE_50 = 0x01a5
    PAIRED_MODULE_51 = 0x01a6
    PAIRED_MODULE_52 = 0x01a7
    PAIRED_MODULE_53 = 0x01a8
    PAIRED_MODULE_54 = 0x01a9
    PAIRED_MODULE_55 = 0x01aa
    PAIRED_MODULE_56 = 0x01ab
    PAIRED_MODULE_57 = 0x01ac
    PAIRED_MODULE_58 = 0x01ad
    PAIRED_MODULE_59 = 0x01ae
    PAIRED_MODULE_60 = 0x01af
    PAIRED_MODULE_61 = 0x01b0
    PAIRED_MODULE_62 = 0x01b1
    PAIRED_MODULE_63 = 0x01b2
    PAIRED_MODULE_64 = 0x01b3
    PAIRED_MODULE_65 = 0x01b4
    PAIRED_MODULE_66 = 0x01b5
    PAIRED_MODULE_67 = 0x01b6
    PAIRED_MODULE_68 = 0x01b7
    PAIRED_MODULE_69 = 0x01b8
    PAIRED_MODULE_70 = 0x01b9
    PAIRED_MODULE_71 = 0x01ba
    PAIRED_MODULE_72 = 0x01bb
    PAIRED_MODULE_73 = 0x01bc
    PAIRED_MODULE_74 = 0x01bd
    PAIRED_MODULE_75 = 0x01be
    PAIRED_MODULE_76 = 0x01bf
    PAIRED_MODULE_77 = 0x01c0
    PAIRED_MODULE_78 = 0x01c1
    PAIRED_MODULE_79 = 0x01c2
    PAIRED_MODULE_80 = 0x01c3
    PAIRED_MODULE_81 = 0x01c4
    PAIRED_MODULE_82 = 0x01c5
    PAIRED_MODULE_83 = 0x01c6
    PAIRED_MODULE_84 = 0x01c7
    PAIRED_MODULE_85 = 0x01c8
    PAIRED_MODULE_86 = 0x01c9
    PAIRED_MODULE_87 = 0x01ca
    PAIRED_MODULE_88 = 0x01cb
    PAIRED_MODULE_89 = 0x01cc
    PAIRED_MODULE_90 = 0x01cd
    PAIRED_MODULE_91 = 0x01ce
    PAIRED_MODULE_92 = 0x01cf
    PAIRED_MODULE_93 = 0x01d0
    PAIRED_MODULE_94 = 0x01d1
    PAIRED_MODULE_95 = 0x01d2
    PAIRED_MODULE_96 = 0x01d3
    PAIRED_MODULE_97 = 0x01d4
    PAIRED_MODULE_98 = 0x01d5
    PAIRED_MODULE_99 = 0x01d6
    PAIRED_MODULE_100 = 0x01d7
    PAIRED_MODULE_101 = 0x01d8
    PAIRED_MODULE_102 = 0x01d9
    PAIRED_MODULE_103 = 0x01da
    PAIRED_MODULE_104 = 0x01db
    PAIRED_MODULE_105 = 0x01dc
    PAIRED_MODULE_106 = 0x01dd
    PAIRED_MODULE_107 = 0x01de
    PAIRED_MODULE_108 = 0x01df
    PAIRED_MODULE_109 = 0x01e0
    PAIRED_MODULE_110 = 0x01e1
    PAIRED_MODULE_111 = 0x01e2
    PAIRED_MODULE_112 = 0x01e3
    PAIRED_MODULE_113 = 0x01e4
    PAIRED_MODULE_114 = 0x01e5
    PAIRED_MODULE_115 = 0x01e6
    PAIRED_MODULE_116 = 0x01e7
    PAIRED_MODULE_117 = 0x01e8
    PAIRED_MODULE_118 = 0x01e9
    PAIRED_MODULE_119 = 0x01ea
    PAIRED_MODULE_120 = 0x01eb
    PAIRED_MODULE_121 = 0x01ec
    PAIRED_MODULE_122 = 0x01ed
    PAIRED_MODULE_123 = 0x01ee
    PAIRED_MODULE_124 = 0x01ef
    PAIRED_MODULE_125 = 0x01f0
    PAIRED_MODULE_126 = 0x01f1
    PAIRED_MODULE_127 = 0x01f2
    COMBI_1_STATUS_SLAVE_ID = 0x01f3
    COMBI_2_STATUS_SLAVE_ID = 0x01f4
    COMBI_3_STATUS_SLAVE_ID = 0x01f5
    COMBI_4_STATUS_SLAVE_ID = 0x01f6
    NUM_OF_GEMINI_SLV = 0x01f7
    GEMINI_SLV_ID0 = 0x01f8
    GEMINI_SLV_ID1 = 0x01f9
    GEMINI_SLV_ID2 = 0x01fa
    GEMINI_SLV_ID3 = 0x01fb
    GEMINI_SLV_ID4 = 0x01fc
    GEMINI_SLV_ID5 = 0x01fd
    GEMINI_SLV_ID6 = 0x01fe
    GEMINI_SLV_ID7 = 0x01ff
    GEMINI_RS485_SLAVE_DETECT_PERIOD = 0x0200
    GEMINI_RS485_SLAVE_DETECT_LOOPS = 0x0201
    GEMINI_RS485_MASTER_GRANT_SLOT = 0x0202
    GEMINI_STREAM_COMBIS = 0x0203
    ERROR_LOG_1_TIME = 0x0204
    ERROR_LOG_1_CODE = 0x0205
    ERROR_LOG_2_TIME = 0x0206
    ERROR_LOG_2_CODE = 0x0207
    ERROR_LOG_3_TIME = 0x0208
    ERROR_LOG_3_CODE = 0x0209
    ERROR_LOG_4_TIME = 0x020a
    ERROR_LOG_4_CODE = 0x020b
    ERROR_LOG_5_TIME = 0x020c
    ERROR_LOG_5_CODE = 0x020d
    WARNING_LOG_1_TIME = 0x020e
    WARNING_LOG_1_CODE = 0x020f
    WARNING_LOG_2_TIME = 0x0210
    WARNING_LOG_2_CODE = 0x0211
    WARNING_LOG_3_TIME = 0x0212
    WARNING_LOG_3_CODE = 0x0213
    WARNING_LOG_4_TIME = 0x0214
    WARNING_LOG_4_CODE = 0x0215
    WARNING_LOG_5_TIME = 0x0216
    WARNING_LOG_5_CODE = 0x0217
    POWER_REDUCER_PERCENTAGE_0 = 0x0218
    POWER_REDUCER_COSPHI_0 = 0x0219
    POWER_REDUCER_PERCENTAGE_1 = 0x021a
    POWER_REDUCER_COSPHI_1 = 0x021b
    POWER_REDUCER_PERCENTAGE_2 = 0x021c
    POWER_REDUCER_COSPHI_2 = 0x021d
    POWER_REDUCER_PERCENTAGE_3 = 0x021e
    POWER_REDUCER_COSPHI_3 = 0x021f
    POWER_REDUCER_PERCENTAGE_4 = 0x0220
    POWER_REDUCER_COSPHI_4 = 0x0221
    POWER_REDUCER_PERCENTAGE_5 = 0x0222
    POWER_REDUCER_COSPHI_5 = 0x0223
    POWER_REDUCER_PERCENTAGE_6 = 0x0224
    POWER_REDUCER_COSPHI_6 = 0x0225
    POWER_REDUCER_PERCENTAGE_7 = 0x0226
    POWER_REDUCER_COSPHI_7 = 0x0227
    POWER_REDUCER_PERCENTAGE_8 = 0x0228
    POWER_REDUCER_COSPHI_8 = 0x0229
    POWER_REDUCER_PERCENTAGE_9 = 0x022a
    POWER_REDUCER_COSPHI_9 = 0x022b
    POWER_REDUCER_PERCENTAGE_10 = 0x022c
    POWER_REDUCER_COSPHI_10 = 0x022d
    POWER_REDUCER_PERCENTAGE_11 = 0x022e
    POWER_REDUCER_COSPHI_11 = 0x022f
    POWER_REDUCER_PERCENTAGE_12 = 0x0230
    POWER_REDUCER_COSPHI_12 = 0x0231
    POWER_REDUCER_PERCENTAGE_13 = 0x0232
    POWER_REDUCER_COSPHI_13 = 0x0233
    POWER_REDUCER_PERCENTAGE_14 = 0x0234
    POWER_REDUCER_COSPHI_14 = 0x0235
    POWER_REDUCER_PERCENTAGE_15 = 0x0236
    POWER_REDUCER_COSPHI_15 = 0x0237


class PolestarMessageType(enum.Enum):
    CMD_POLESTAR_MAC_ADDR_GET = 0x0306
    CMD_POLESTAR_IP_ADDR_GET = 0x0307
    CMD_POLESTAR_SEND_PING = 0x030c
    CMD_POLESTAR_CONFTOOL_START = 0x030e
    CMD_POLESTAR_ETHERNET_STAT = 0x030f
    CMD_POLESTAR_GET_POK_STATUS = 0x031c
    CMD_POLESTAR_ZB_PRESENT_STATUS = 0x031e
    CMD_POLESTAR_GET_S_OK_STATUS = 0x0321
    CMD_POLESTAR_GET_ENERGY_STATISTICS_STATUS = 0x0322
    CMD_POLESTAR_BLOCK_SERVER_CONTROL = 0x0329
    CMD_POLESTAR_GET_SERVER_CONTROL_STATUS = 0x032a
    RESP_POLESTAR_MAC_ADDR_GET = 0x0381
    RESP_POLESTAR_IP_ADDR_GET = 0x0382
    RESP_POLESTAR_SEND_PING = 0x0383
    RESP_POLESTAR_ETHERNET_STAT = 0x0384
    RESP_POLESTAR_GET_POK_STATUS = 0x0388
    RESP_POLESTAR_GET_S_OK_STATUS = 0x038c
    RESP_POLESTAR_GET_ENERGY_STATISTICS_STATUS = 0x038d
    RESP_POLESTAR_GET_SERVER_CONTROL_STATUS = 0x0392