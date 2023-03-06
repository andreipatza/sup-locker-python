# import libraries
import RPi.GPIO as GPIO

# https://sourceforge.net/p/raspberry-gpio-python/wiki/Inputs/

# DEFINITION OF OUTPUT PINS
DXX_ON = 3              # 3 = DXX_ON              DEFAULT 0
S0 = 5                  # 5 = S0                  DEFAULT 0
S1 = 7                  # 7 = S1                  DEFAULT 0
S2 = 11                 # 11 = S2                 DEFAULT 0
S3 = 12                 # 12 = S3                 DEFAULT 0
EN_DXX_ON = 13          # 13 = EN_DXX_ON          DEFAULT 1
STATUS_COMMAND = 16     # 16 = STATUS_COMMAND     DEFAULT 0
LED_ON_X = 18           # 18 = LED_ON_X           DEFAULT 0
IN1 = 23                # 23 = IN1                DEFAULT 0
IN2 = 24                # 24 = IN2                DEFAULT 0
IN3 = 26                # 26 = IN3                DEFAULT 0
IN4 = 29                # 29 = IN4                DEFAULT 0

# DEFINITION OF INPUT PINS
STATUS_DOOR_X = 15     # 15 = STATUS_DOOR_X
STATUS_SENSOR1_X = 19  # 19 = STATUS_SENSOR1_X
STATUS_SENSOR2_X = 21  # 21 = STATUS_SENSOR2_X
STATUS_SENSOR3_X = 22  # 22 = STATUS_SENSOR3_X


def initializePins():
    # INITIALIZE OUTPUT PINS
    GPIO.setup(DXX_ON, GPIO.OUT)
    GPIO.output(DXX_ON, GPIO.LOW)

    GPIO.setup(S0, GPIO.OUT)
    GPIO.output(S0, GPIO.LOW)

    GPIO.setup(S1, GPIO.OUT)
    GPIO.output(S1, GPIO.LOW)

    GPIO.setup(S2, GPIO.OUT)
    GPIO.output(S2, GPIO.LOW)

    GPIO.setup(S3, GPIO.OUT)
    GPIO.output(S3, GPIO.LOW)

    GPIO.setup(EN_DXX_ON, GPIO.OUT)
    GPIO.output(EN_DXX_ON, GPIO.HIGH)

    GPIO.setup(STATUS_COMMAND, GPIO.OUT)
    GPIO.output(STATUS_COMMAND, GPIO.LOW)

    GPIO.setup(LED_ON_X, GPIO.OUT)
    GPIO.output(LED_ON_X, GPIO.LOW)

    GPIO.setup(IN1, GPIO.OUT)
    GPIO.output(IN1, GPIO.LOW)

    GPIO.setup(IN2, GPIO.OUT)
    GPIO.output(IN2, GPIO.LOW)

    GPIO.setup(IN3, GPIO.OUT)
    GPIO.output(IN3, GPIO.LOW)

    GPIO.setup(IN4, GPIO.OUT)
    GPIO.output(IN4, GPIO.LOW)

    # INITIALIZE INPUT PINS
    GPIO.setup(STATUS_DOOR_X, GPIO.IN)
    GPIO.setup(STATUS_SENSOR1_X, GPIO.IN)
    GPIO.setup(STATUS_SENSOR2_X, GPIO.IN)
    GPIO.setup(STATUS_SENSOR3_X, GPIO.IN)


def setPinVoltage(pin, voltage):
    if voltage == "HIGH":
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)


def readPinVoltage(pin):
    return GPIO.input(pin)
