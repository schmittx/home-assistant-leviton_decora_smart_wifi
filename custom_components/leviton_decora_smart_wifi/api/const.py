"""Leviton API"""
API_ENDPOINT = "https://my.leviton.com/api"

LOGIN_CODE_INVALID = "login_code_invalid"
LOGIN_CODE_REQUIRED = "login_code_required"
LOGIN_FAILED = "login_failed"
LOGIN_SUCCESS = "login_success"
LOGIN_TOO_MANY_ATTEMPTS = "login_too_many_attempts"

CONTROL_TIMING_NORMAL = "normal"
CONTROL_TIMING_MEDIUM = "medium"
CONTROL_TIMING_EXTENDED = "extended"
CONTROL_TIMING_UNKNOWN = "unknown"

CONTROL_TIMING_MAP = {
    80: CONTROL_TIMING_NORMAL,
    92: CONTROL_TIMING_MEDIUM,
    97: CONTROL_TIMING_EXTENDED,
}

GFCI_STATUS_FAULT = "fault"
GFCI_STATUS_PROTECTED = "protected"
GFCI_STATUS_TEST = "test"
GFCI_STATUS_UNKNOWN = "unknown"

GFCI_STATUS_MAP = {
    "": GFCI_STATUS_PROTECTED,
    "GFCI_FAULT": GFCI_STATUS_FAULT,
    "MANUAL_TRIP": GFCI_STATUS_TEST,
}

GFCI_STATUS_OPTIONS = [
    GFCI_STATUS_FAULT,
    GFCI_STATUS_PROTECTED,
    GFCI_STATUS_TEST,
    GFCI_STATUS_UNKNOWN,
]

DEVICE_MODEL = "model"
DEVICE_TYPE = "type"
DEVICE_GENERATION = "generation"

DEVICE_TYPE_CONTROLLER = "controller"
DEVICE_TYPE_FAN = "fan"
DEVICE_TYPE_GFCI = "gfci"
DEVICE_TYPE_LIGHT = "light"
DEVICE_TYPE_OUTLET = "outlet"
DEVICE_TYPE_SWITCH = "switch"

DEVICE_GENERATION_1 = 1
DEVICE_GENERATION_2 = 2

SUPPORTED_DEVICES = [
    {
        DEVICE_MODEL: "D215O",
        DEVICE_TYPE: [DEVICE_TYPE_OUTLET],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "D215P",
        DEVICE_TYPE: [DEVICE_TYPE_OUTLET],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "D215R",
        DEVICE_TYPE: [DEVICE_TYPE_OUTLET],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "D215S",
        DEVICE_TYPE: [DEVICE_TYPE_SWITCH],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "D23LP",
        DEVICE_TYPE: [DEVICE_TYPE_LIGHT],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "D24SF",
        DEVICE_TYPE: [DEVICE_TYPE_FAN],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "D26HD",
        DEVICE_TYPE: [DEVICE_TYPE_LIGHT],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "D2ELV",
        DEVICE_TYPE: [DEVICE_TYPE_LIGHT],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "D2GF1",
        DEVICE_TYPE: [DEVICE_TYPE_GFCI],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "D2MSD",
        DEVICE_TYPE: [DEVICE_TYPE_LIGHT],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "D2SCS",
        DEVICE_TYPE: [DEVICE_TYPE_CONTROLLER, DEVICE_TYPE_SWITCH],
        DEVICE_GENERATION: DEVICE_GENERATION_2,
    },
    {
        DEVICE_MODEL: "DW15A",
        DEVICE_TYPE: [DEVICE_TYPE_OUTLET],
        DEVICE_GENERATION: DEVICE_GENERATION_1,
    },
    {
        DEVICE_MODEL: "DW15P",
        DEVICE_TYPE: [DEVICE_TYPE_OUTLET],
        DEVICE_GENERATION: DEVICE_GENERATION_1,
    },
    {
        DEVICE_MODEL: "DW15R",
        DEVICE_TYPE: [DEVICE_TYPE_OUTLET],
        DEVICE_GENERATION: DEVICE_GENERATION_1,
    },
    {
        DEVICE_MODEL: "DW15S",
        DEVICE_TYPE: [DEVICE_TYPE_SWITCH],
        DEVICE_GENERATION: DEVICE_GENERATION_1,
    },
    {
        DEVICE_MODEL: "DW1KD",
        DEVICE_TYPE: [DEVICE_TYPE_LIGHT],
        DEVICE_GENERATION: DEVICE_GENERATION_1,
    },
    {
        DEVICE_MODEL: "DW1KD",
        DEVICE_TYPE: [DEVICE_TYPE_LIGHT],
        DEVICE_GENERATION: DEVICE_GENERATION_1,
    },
    {
        DEVICE_MODEL: "DW4BC",
        DEVICE_TYPE: [DEVICE_TYPE_CONTROLLER],
        DEVICE_GENERATION: DEVICE_GENERATION_1,
    },
    {
        DEVICE_MODEL: "DW4SF",
        DEVICE_TYPE: [DEVICE_TYPE_FAN],
        DEVICE_GENERATION: DEVICE_GENERATION_1,
    },
    {
        DEVICE_MODEL: "DW6HD",
        DEVICE_TYPE: [DEVICE_TYPE_LIGHT],
        DEVICE_GENERATION: DEVICE_GENERATION_1,
    },
    {
        DEVICE_MODEL: "DWVAA",
        DEVICE_TYPE: [DEVICE_TYPE_LIGHT],
        DEVICE_GENERATION: DEVICE_GENERATION_1,
    },
]

SUPPORTED_DEVICES_CONTROLLER = [device[DEVICE_MODEL] for device in SUPPORTED_DEVICES if DEVICE_TYPE_CONTROLLER in device[DEVICE_TYPE]]
SUPPORTED_DEVICES_FAN = [device[DEVICE_MODEL] for device in SUPPORTED_DEVICES if DEVICE_TYPE_FAN in device[DEVICE_TYPE]]
SUPPORTED_DEVICES_GFCI = [device[DEVICE_MODEL] for device in SUPPORTED_DEVICES if DEVICE_TYPE_GFCI in device[DEVICE_TYPE]]
SUPPORTED_DEVICES_LIGHT = [device[DEVICE_MODEL] for device in SUPPORTED_DEVICES if DEVICE_TYPE_LIGHT in device[DEVICE_TYPE]]
SUPPORTED_DEVICES_OUTLET = [device[DEVICE_MODEL] for device in SUPPORTED_DEVICES if DEVICE_TYPE_OUTLET in device[DEVICE_TYPE]]
SUPPORTED_DEVICES_SWITCH = [device[DEVICE_MODEL] for device in SUPPORTED_DEVICES if DEVICE_TYPE_SWITCH in device[DEVICE_TYPE]]

SECOND_GENERATION_DEVICES = [device[DEVICE_MODEL] for device in SUPPORTED_DEVICES if device[DEVICE_GENERATION] == DEVICE_GENERATION_2]

STATUS_AWAY = "away"
STATUS_HOME = "home"
STATUS_UNKNOWN = "unknown"

STATUS_MAP = {
    "AWAY": STATUS_AWAY,
    "HOME": STATUS_HOME,
}

STATUS_LED_MODE_OFF = "led_always_off"
STATUS_LED_MODE_STATUS = "status_mode"
STATUS_LED_MODE_LOCATOR = "locator_mode"
STATUS_LED_MODE_UNKNOWN = "unknown"

STATUS_LED_MODE_MAP = {
    0: STATUS_LED_MODE_OFF,
    254: STATUS_LED_MODE_STATUS,
    255: STATUS_LED_MODE_LOCATOR,
}

STATUS_LED_ENABLED = 255
STATUS_LED_DISABLED = 0

DIM_LED_MODE_OFF = "always_off"
DIM_LED_MODE_ON = "always_on"

DIMMING_MODE_FORWARD = "forward"
DIMMING_MODE_REVERSE = "reverse"
DIMMING_MODE_UNKNOWN = "unknown"

TIME_PERIOD_0_SECONDS = "0_seconds"
TIME_PERIOD_0_5_SECONDS = "0_5_seconds"
TIME_PERIOD_1_SECOND = "1_second"
TIME_PERIOD_1_5_SECONDS = "1_5_seconds"
TIME_PERIOD_2_SECONDS = "2_seconds"
TIME_PERIOD_3_SECONDS = "3_seconds"
TIME_PERIOD_5_SECONDS = "5_seconds"
TIME_PERIOD_10_SECONDS = "10_seconds"
TIME_PERIOD_15_SECONDS = "15_seconds"
TIME_PERIOD_25_SECONDS = "25_seconds"

TIME_PERIOD_1_MINUTE = "1_minute"
TIME_PERIOD_2_MINUTES = "2_minutes"
TIME_PERIOD_3_MINUTES = "3_minutes"
TIME_PERIOD_4_MINUTES = "4_minutes"
TIME_PERIOD_5_MINUTES = "5_minutes"
TIME_PERIOD_6_MINUTES = "6_minutes"
TIME_PERIOD_7_MINUTES = "7_minutes"
TIME_PERIOD_8_MINUTES = "8_minutes"
TIME_PERIOD_9_MINUTES = "9_minutes"
TIME_PERIOD_10_MINUTES = "10_minutes"
TIME_PERIOD_15_MINUTES = "15_minutes"
TIME_PERIOD_20_MINUTES = "20_minutes"
TIME_PERIOD_25_MINUTES = "25_minutes"
TIME_PERIOD_30_MINUTES = "30_minutes"
TIME_PERIOD_45_MINUTES = "45_minutes"
TIME_PERIOD_60_MINUTES = "60_minutes"

TIME_PERIOD_1_HOUR = "1_hour"
TIME_PERIOD_2_HOURS = "2_hours"
TIME_PERIOD_3_HOURS = "3_hours"
TIME_PERIOD_4_HOURS = "4_hours"
TIME_PERIOD_5_HOURS = "5_hours"
TIME_PERIOD_6_HOURS = "6_hours"
TIME_PERIOD_7_HOURS = "7_hours"
TIME_PERIOD_8_HOURS = "8_hours"
TIME_PERIOD_9_HOURS = "9_hours"
TIME_PERIOD_10_HOURS = "10_hours"
TIME_PERIOD_11_HOURS = "11_hours"
TIME_PERIOD_12_HOURS = "12_hours"
TIME_PERIOD_24_HOURS = "24_hours"

TIME_PERIOD_UNKNOWN = "unknown"

DIM_LED_MAP = {
    0: DIM_LED_MODE_OFF,
    1: TIME_PERIOD_1_SECOND,
    2: TIME_PERIOD_2_SECONDS,
    3: TIME_PERIOD_3_SECONDS,
    5: TIME_PERIOD_5_SECONDS,
    10: TIME_PERIOD_10_SECONDS,
    15: TIME_PERIOD_15_SECONDS,
    25: TIME_PERIOD_25_SECONDS,
    255: DIM_LED_MODE_ON,
}

LOAD_TYPE_ELV = "elv"
LOAD_TYPE_INCANDESCENT = "incandescent"
LOAD_TYPE_LED = "led"
LOAD_TYPE_CFL = "cfl"
LOAD_TYPE_NON_DIMMABLE = "non_dimmable"
LOAD_TYPE_MLV = "mlv"
LOAD_TYPE_UNKNOWN = "unknown"

LOAD_TYPE_MAP = {
    0: LOAD_TYPE_INCANDESCENT,
    1: LOAD_TYPE_LED,
    2: LOAD_TYPE_CFL,
    4: LOAD_TYPE_MLV,
    5: LOAD_TYPE_NON_DIMMABLE,
    6: LOAD_TYPE_ELV,
}

FADE_ON_OFF_RATE_MAP = {
    0: TIME_PERIOD_0_SECONDS,
    5: TIME_PERIOD_0_5_SECONDS,
    10: TIME_PERIOD_1_SECOND,
    15: TIME_PERIOD_1_5_SECONDS,
    20: TIME_PERIOD_2_SECONDS,
    30: TIME_PERIOD_3_SECONDS,
    50: TIME_PERIOD_5_SECONDS,
    100: TIME_PERIOD_10_SECONDS,
    150: TIME_PERIOD_15_SECONDS,
    250: TIME_PERIOD_25_SECONDS,
}

MINIMUM_AMBIENT_THRESHOLD = 1
MINIMUM_LEVEL_FAN = 25
MINIMUM_LEVEL_LIGHT = 1
MAXIMUM_LEVEL = 100

STEP_LEVEL_FAN = 25
STEP_LEVEL_LIGHT = 1

PRESET_LEVEL_OFF = 0

AUTO_SHUTOFF_DISABLED = "disabled"

AUTO_SHUTOFF_MAP = {
    0: AUTO_SHUTOFF_DISABLED,
    60: TIME_PERIOD_1_MINUTE,
    300: TIME_PERIOD_5_MINUTES,
    600: TIME_PERIOD_10_MINUTES,
    900: TIME_PERIOD_15_MINUTES,
    1800: TIME_PERIOD_30_MINUTES,
    3600: TIME_PERIOD_1_HOUR,
    7200: TIME_PERIOD_2_HOURS,
    10800: TIME_PERIOD_3_HOURS,
    14400: TIME_PERIOD_4_HOURS,
    18000: TIME_PERIOD_5_HOURS,
    21600: TIME_PERIOD_6_HOURS,
    25200: TIME_PERIOD_7_HOURS,
    28800: TIME_PERIOD_8_HOURS,
    32400: TIME_PERIOD_9_HOURS,
    36000: TIME_PERIOD_10_HOURS,
    39600: TIME_PERIOD_11_HOURS,
    43200: TIME_PERIOD_12_HOURS,
}

MOTION_NIGHT_MODE_ROOM = "room_lights"
MOTION_NIGHT_MODE_GUIDE = "guidelight"
MOTION_NIGHT_MODE_UNKNOWN = "unknown"

MOTION_NIGHT_MODE_MAP = {
    0: MOTION_NIGHT_MODE_ROOM,
    2: MOTION_NIGHT_MODE_GUIDE,
}

MOTION_MODE_OCCUPANCY = "occupancy"
MOTION_MODE_VACANCY = "vacancy"
MOTION_MODE_UNKNOWN = "unknown"

MOTION_MODE_MAP = {
    0: MOTION_MODE_OCCUPANCY,
    1: MOTION_MODE_VACANCY,
}

MOTION_SNOOZE_DISABLED = "disabled"
MOTION_SNOOZE_UNKNOWN = "unknown"

MOTION_SNOOZE_MAP = {
    0: MOTION_SNOOZE_DISABLED,
    1: TIME_PERIOD_1_MINUTE,
    5: TIME_PERIOD_5_MINUTES,
    10: TIME_PERIOD_10_MINUTES,
    15: TIME_PERIOD_15_MINUTES,
    30: TIME_PERIOD_30_MINUTES,
    60: TIME_PERIOD_1_HOUR,
    120: TIME_PERIOD_2_HOURS,
    180: TIME_PERIOD_3_HOURS,
    240: TIME_PERIOD_4_HOURS,
    300: TIME_PERIOD_5_HOURS,
    360: TIME_PERIOD_6_HOURS,
    420: TIME_PERIOD_7_HOURS,
    480: TIME_PERIOD_8_HOURS,
    540: TIME_PERIOD_9_HOURS,
    600: TIME_PERIOD_10_HOURS,
    660: TIME_PERIOD_11_HOURS,
    720: TIME_PERIOD_12_HOURS,
    1440: TIME_PERIOD_24_HOURS,
}

MOTION_TIMEOUT_MAP = {
    1: TIME_PERIOD_1_MINUTE,
    2: TIME_PERIOD_2_MINUTES,
    3: TIME_PERIOD_3_MINUTES,
    4: TIME_PERIOD_4_MINUTES,
    5: TIME_PERIOD_5_MINUTES,
    6: TIME_PERIOD_6_MINUTES,
    7: TIME_PERIOD_7_MINUTES,
    8: TIME_PERIOD_8_MINUTES,
    9: TIME_PERIOD_9_MINUTES,
    10: TIME_PERIOD_10_MINUTES,
    15: TIME_PERIOD_15_MINUTES,
    20: TIME_PERIOD_20_MINUTES,
    25: TIME_PERIOD_25_MINUTES,
    30: TIME_PERIOD_30_MINUTES,
    45: TIME_PERIOD_45_MINUTES,
    60: TIME_PERIOD_60_MINUTES,
}

MOTION_TIMEOUT_UNKNOWN = "unknown"

POWER_OFF = "OFF"
POWER_ON = "ON"