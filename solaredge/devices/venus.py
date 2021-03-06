import enum


class VenusParameters(enum.Enum):
    ID = 0x0000
    VERSION_MAJOR = 0x0001
    VERSION_MINOR = 0x0002
    VERSION_CHECKSUM = 0x0003
    VENUSPWR_VERSION_MAJOR = 0x0004
    VENUSPWR_VERSION_MINOR = 0x0005
    VTELEM_TIME = 0x0006
    INV_COUNTRY_CODE = 0x0007
    VERSION_BUILD = 0x0008
    RESERVED0 = 0x0009
    INV_PRODUCT_MODEL = 0x000a
    ISE_DSP_DISABLE = 0x000b
    VIN_MISMATCH_RESET_TIME = 0x000c
    INV_SET_ISE_INV_PARAMS_TO_BOUNDARIES = 0x000d
    RESERVED1 = 0x000e
    RESERVED2 = 0x000f
    SUPERVISE_ENABLE = 0x0010
    MIN_VIN = 0x0011
    VIN_NIGHT = 0x0012
    VIN_NIGHT_TIMEOUT_MSEC = 0x0013
    LOW_POWER_MODE_ENABLED = 0x0014
    LOW_POWER_MODE_CHECK_VIN_INTERVAL = 0x0015
    RELAYS_CLOSE_HOLDOFF_TIME = 0x0016
    RELAYS_SMART_MONITOR_ENABLED = 0x0017
    GRID_MON_SKIP_ENABLE = 0x0018
    INV_US_L1L2_VS_L1N_THRESH = 0x0019
    INVGRID_CONVERSION_MODE = 0x001a
    INVGRID_CONFIGURATION = 0x001b
    INVGRID_I_RCD_STEP = 0x001c
    INVGRID_I_RCD_MAX = 0x001d
    INVGRID_STEP_TIME = 0x001e
    INVGRID_VOUT_MAX = 0x001f
    INVGRID_VOUT_MIN = 0x0020
    INVGRID_VOUT_MAX2 = 0x0021
    INVGRID_VOUT_MIN2 = 0x0022
    INVGRID_VLXN_MAX = 0x0023
    INVGRID_VLXN_MIN = 0x0024
    INVGRID_VOUT_MAX_HOLD_OFF_TIME = 0x0025
    INVGRID_VOUT_MIN_HOLD_OFF_TIME = 0x0026
    INVGRID_VOUT_MAX_HOLD_OFF_TIME2 = 0x0027
    INVGRID_VOUT_MIN_HOLD_OFF_TIME2 = 0x0028
    INVGRID_VLXN_HOLD_OFF_TIME = 0x0029
    INVGRID_F_GRID_MAX = 0x002a
    INVGRID_F_GRID_MIN = 0x002b
    INVGRID_F_HOLD_OFF_TIME = 0x002c
    INVGRID_R_ISO = 0x002d
    INVGRID_I_OUT_DC_MAX = 0x002e
    INVGRID_I_OUT_DC_HOLD_OFF_TIME = 0x002f
    INVGRID_T_REST = 0x0030
    INVGRID_I_CTRL_MAX = 0x0031
    INVGRID_WAKEUP_VOLTAGE = 0x0032
    INVGRID_DUTY_CYCLE = 0x0033
    INVGRID_OUTPUT_FREQ = 0x0034
    INVGRID_SINUS_OR_FIXED_DUTY_CYCLE = 0x0035
    INVGRID_MAX_ACTIVE_POWER = 0x0036
    INVGRID_TEMPRATURE_DERATING_START = 0x0037
    INVGRID_TEMPRATURE_DERATING_RANGE = 0x0038
    INVGRID_GRID_MONITOR_TIME = 0x0039
    INVGRID_DC_VOLTAGE_REF = 0x003a
    INVGRID_MPP_TRACK = 0x003b
    INVGRID_MPP_TRACK_TIME = 0x003c
    INVGRID_MPP_MIN = 0x003d
    INVGRID_MPP_MAX = 0x003e
    INVGRID_DCO_MIN_VOLTAGE = 0x003f
    I_ERR_MAX_10_MA = 0x0040
    LOW_PWR_TIME_S = 0x0041
    FG_DEV_STEP_10_MHZ = 0x0042
    RESERVED3 = 0x0043
    RESERVED4 = 0x0044
    RESERVED5 = 0x0045
    KA_VIN_REF = 0x0046
    KA_VIN_MAX = 0x0047
    KA_CHANGE_WORD = 0x0048
    KA_NOCHANGE_WORD = 0x0049
    KA_PACKET_MODE = 0x004a
    KA_PACKET_TOTAL_LEN = 0x004b
    KA_PACKET_NUM_BARKERS = 0x004c
    KA_SIGNAL_STRENGTH = 0x004d
    KA_SIGNAL_LOCK_ITER_FACTOR = 0x004e
    KA_SIGNAL_LOCK_ITER_TIME = 0x004f
    DEBUG_DOT = 0x0050
    DEBUG_PANEL_TELEM = 0x0051
    DEBUG_INV_EVENTS = 0x0052
    DEBUG_TX_LOOP = 0x0053
    RESERVED6 = 0x0054
    WATCHDOG_ENABLE = 0x0055
    TX_FREQ0 = 0x0056
    TX_FREQ1 = 0x0057
    TX_BITRATE = 0x0058
    TX_AMP_DB = 0x0059
    RX_FREQ0 = 0x005a
    RX_FREQ1 = 0x005b
    RX_BITRATE = 0x005c
    RX_SNR_THRESH = 0x005d
    RX_DC_FILTER_ZEROES = 0x005e
    RX_FILTER_FREQ = 0x005f
    RX_ANALOG_AGC = 0x0060
    CURRENT_MODEM_BIT_RATE = 0x0061
    CURRENT_MODEM_ZERO_BIT_TIME = 0x0062
    CURRENT_MODEM_MAX_SAFETY_VOLTAGE = 0x0063
    PAIRING_TX_RANDOM_RANGE = 0x0064
    PAIRING_RX_RANDOM_RANGE = 0x0065
    PAIRING_TX_RANDOM = 0x0066
    PAIRING_TX_MANUAL = 0x0067
    PAIRING_RX_RANDOM = 0x0068
    PAIRING_RX_MANUAL = 0x0069
    PAIRING_TX_FREQ0_0 = 0x006a
    PAIRING_TX_FREQ0_1 = 0x006b
    PAIRING_TX_FREQ1_0 = 0x006c
    PAIRING_TX_FREQ1_1 = 0x006d
    PAIRING_TX_FREQ2_0 = 0x006e
    PAIRING_TX_FREQ2_1 = 0x006f
    PAIRING_TX_FREQ3_0 = 0x0070
    PAIRING_TX_FREQ3_1 = 0x0071
    FREQ_50_HZ_JET_V1 = 0x0072
    FREQ_50_HZ_JET_V2 = 0x0073
    FREQ_50_HZ_JET_V3 = 0x0074
    FREQ_50_HZ_JET_MIN_COS_PHI = 0x0075
    FREQ_50_HZ_JET_MIN_POWER_PERCENT = 0x0076
    FREQ_50_HZ_JET_ALPHA = 0x0077
    FREQ_60_HZ_JET_V1 = 0x0078
    FREQ_60_HZ_JET_V2 = 0x0079
    FREQ_60_HZ_JET_V3 = 0x007a
    FREQ_60_HZ_JET_MIN_COS_PHI = 0x007b
    FREQ_60_HZ_JET_MIN_POWER_PERCENT = 0x007c
    FREQ_60_HZ_JET_ALPHA = 0x007d
    LAST_TELEM_SNR = 0x007e
    TX_SIG_STRENGTH = 0x007f
    RX_SIG_STRENGTH = 0x0080
    SE_RSV_0 = 0x0081
    SE_RSV_1 = 0x0082
    SE_RSV_2 = 0x0083
    SE_RSV_3 = 0x0084
    SE_RSV_4 = 0x0085
    SE_RSV_5 = 0x0086
    SE_RSV_6 = 0x0087
    PAIRING_TX_FREQ4_0 = 0x0088
    PAIRING_TX_FREQ4_1 = 0x0089
    PAIRING_TX_FREQ5_0 = 0x008a
    PAIRING_TX_FREQ5_1 = 0x008b
    PAIRING_TX_FREQ6_0 = 0x008c
    PAIRING_TX_FREQ6_1 = 0x008d
    PAIRING_TX_FREQ7_0 = 0x008e
    PAIRING_TX_FREQ7_1 = 0x008f
    PAIRING_TX_FREQ8_0 = 0x0090
    PAIRING_TX_FREQ8_1 = 0x0091
    PAIRING_TX_FREQ9_0 = 0x0092
    PAIRING_TX_FREQ9_1 = 0x0093
    PAIRING_TX_FREQ10_0 = 0x0094
    PAIRING_TX_FREQ10_1 = 0x0095
    PAIRING_TX_FREQ11_0 = 0x0096
    PAIRING_TX_FREQ11_1 = 0x0097
    PAIRING_TX_FREQ12_0 = 0x0098
    PAIRING_TX_FREQ12_1 = 0x0099
    PAIRING_TX_FREQ13_0 = 0x009a
    PAIRING_TX_FREQ13_1 = 0x009b
    PAIRING_TX_FREQ14_0 = 0x009c
    PAIRING_TX_FREQ14_1 = 0x009d
    PAIRING_RX_FREQ0_0 = 0x009e
    PAIRING_RX_FREQ0_1 = 0x009f
    PAIRING_RX_FREQ1_0 = 0x00a0
    PAIRING_RX_FREQ1_1 = 0x00a1
    PAIRING_RX_FREQ2_0 = 0x00a2
    PAIRING_RX_FREQ2_1 = 0x00a3
    PAIRING_RX_FREQ3_0 = 0x00a4
    PAIRING_RX_FREQ3_1 = 0x00a5
    FG_DEV_STEP_10_MHZ_1 = 0x00a6
    POWER_FACTOR_COS_PHI = 0x00a7
    MIN_ACTIVE_POWER = 0x00a8
    MIN_TMP_ADC = 0x00a9
    INVGRID_VIN_MAX = 0x00aa
    INVGRID_VIN_MAX_HOLD_OFF_TIME = 0x00ab
    INVGRID_VIN_MIN = 0x00ac
    INVGRID_VIN_MIN_HOLD_OFF_TIME = 0x00ad
    INVGRID_F_ACTIVE_AVG = 0x00ae
    INVGRID_F_PASSIVE_STEP = 0x00af
    INVGRID_F_PASSIVE_STEP_TIME = 0x00b0
    INVGRID_F_PASSIVE_AVG = 0x00b1
    INVGRID_CONFIGURATION2 = 0x00b2
    ISLANDING_MOVING_AVG_FACTOR = 0x00b3
    ISE_RSV_10 = 0x00b4
    ISE_RSV_11 = 0x00b5
    ISE_RSV_12 = 0x00b6
    ISE_RSV_13 = 0x00b7
    ISE_RSV_14 = 0x00b8
    ISE_RSV_15 = 0x00b9
    ISE_RSV_16 = 0x00ba
    ISE_RSV_17 = 0x00bb
    PAIRING_RX_FREQ4_0 = 0x00bc
    PAIRING_RX_FREQ4_1 = 0x00bd
    PAIRING_RX_FREQ5_0 = 0x00be
    PAIRING_RX_FREQ5_1 = 0x00bf
    PAIRING_RX_FREQ6_0 = 0x00c0
    PAIRING_RX_FREQ6_1 = 0x00c1
    PAIRING_RX_FREQ7_0 = 0x00c2
    PAIRING_RX_FREQ7_1 = 0x00c3
    PAIRING_RX_FREQ8_0 = 0x00c4
    PAIRING_RX_FREQ8_1 = 0x00c5
    PAIRING_RX_FREQ9_0 = 0x00c6
    PAIRING_RX_FREQ9_1 = 0x00c7
    PAIRING_RX_FREQ10_0 = 0x00c8
    PAIRING_RX_FREQ10_1 = 0x00c9
    PAIRING_RX_FREQ11_0 = 0x00ca
    PAIRING_RX_FREQ11_1 = 0x00cb
    PAIRING_RX_FREQ12_0 = 0x00cc
    PAIRING_RX_FREQ12_1 = 0x00cd
    PAIRING_RX_FREQ13_0 = 0x00ce
    PAIRING_RX_FREQ13_1 = 0x00cf
    PAIRING_RX_FREQ14_0 = 0x00d0
    PAIRING_RX_FREQ14_1 = 0x00d1
    LAST_ERROR = 0x00d2
    RESERVED7 = 0x00d3
    RESERVED8 = 0x00d4
    RESERVED9 = 0x00d5
    RESERVED10 = 0x00d6
    MPPT_OP_MODE = 0x00d7
    MPPT_PRINTS = 0x00d8
    MPPT_P_AVG_N = 0x00d9
    MPPT_P_CUT_N_LOW = 0x00da
    MPPT_P_CUT_N_HIGH = 0x00db
    MPPT_VI_MIN = 0x00dc
    MPPT_STEP = 0x00dd
    MPPT_STEP_SHORT_TIME = 0x00de
    MPPT_STEP_LONG_TIME = 0x00df
    MPPT_REF_DELTA_MAX = 0x00e0
    MPPT_MIN_POWER_PERC = 0x00e1
    MPPT_SHORT_K = 0x00e2
    MPPT_LONG_K = 0x00e3
    MPPT_LONG_K_POWER_TH = 0x00e4
    MPPT_LONG_K_PEAKS_TH_LOW = 0x00e5
    MPPT_LONG_K_PEAKS_TH_HIGH = 0x00e6
    MPPT_DYN_STEP_RES = 0x00e7
    MPPT_DYN_STEP_MIN = 0x00e8
    MPPT_DYN_STEP_DELTA = 0x00e9
    MPPT_DYN_STEP_LONG_TIME_MAX = 0x00ea
    MPPT_DYN_STEP_LONG_TIME_DELTA = 0x00eb
    MPPT_PS_AVG_TIME = 0x00ec
    MPPT_PS_MIN_POWER = 0x00ed
    MPPT_PS_MIN_POWER_PERC = 0x00ee
    MPPT_PS_STEP = 0x00ef
    MPPT_PS_STEP_TIME = 0x00f0
    MPPT_PS_SWITCH_PERC = 0x00f1
    MPPT_PS_MAX_SAT_CNT = 0x00f2
    MPPT_PS_QUICK_STEP_RES = 0x00f3


class VenusMessageType(enum.Enum):
    CMD_VENUSMNGR_GET_SYS_STATUS = 0x0205
    CMD_VENUSMNGR_KA_DATA_SEND = 0x0218
    RESP_VENUSMNGR_GET_SYS_STATUS = 0x0283
