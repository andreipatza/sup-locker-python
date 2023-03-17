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
    print('\nSTART___________initializePins method called___________START\n')

    GPIO.setwarnings(False)

    # INITIALIZE OUTPUT PINS
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(DXX_ON, GPIO.OUT)
    print('\nPIN SET:     DXX_ON PIN AS OUTPUT PIN')
    GPIO.output(DXX_ON, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN DXX_ON TO ', 'LOW\n')

    GPIO.setup(S0, GPIO.OUT)
    print('\nPIN SET:     S0 PIN AS OUTPUT PIN')
    GPIO.output(S0, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN S0 TO ', 'LOW\n')

    GPIO.setup(S1, GPIO.OUT)
    print('\nPIN SET:     S1 PIN AS OUTPUT PIN')
    GPIO.output(S1, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN S1 TO ', 'LOW\n')

    GPIO.setup(S2, GPIO.OUT)
    print('\nPIN SET:     S2 PIN AS OUTPUT PIN')
    GPIO.output(S2, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN S2 TO ', 'LOW\n')

    GPIO.setup(S3, GPIO.OUT)
    print('\nPIN SET:     S3 PIN AS OUTPUT PIN')
    GPIO.output(S3, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN S3 TO ', 'LOW\n')

    GPIO.setup(EN_DXX_ON, GPIO.OUT)
    print('\nPIN SET:     EN_DXX_ON PIN AS OUTPUT PIN')
    GPIO.output(EN_DXX_ON, GPIO.HIGH)
    print('VOLTAGE SET: OUTPUT PIN EN_DXX_ON TO ', 'HIGH\n')

    GPIO.setup(STATUS_COMMAND, GPIO.OUT)
    print('\nPIN SET:     STATUS_COMMAND PIN AS OUTPUT PIN')
    GPIO.output(STATUS_COMMAND, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN STATUS_COMMAND TO ', 'LOW\n')

    GPIO.setup(LED_ON_X, GPIO.OUT)
    print('\nPIN SET:     LED_ON_X PIN AS OUTPUT PIN')
    GPIO.output(LED_ON_X, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN LED_ON_X TO ', 'LOW\n')

    GPIO.setup(IN1, GPIO.OUT)
    print('\nPIN SET:     IN1 PIN AS OUTPUT PIN')
    GPIO.output(IN1, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN IN1 TO ', 'LOW\n')

    GPIO.setup(IN2, GPIO.OUT)
    print('\nPIN SET:     IN2 PIN AS OUTPUT PIN')
    GPIO.output(IN2, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN IN2 TO ', 'LOW\n')

    GPIO.setup(IN3, GPIO.OUT)
    print('\nPIN SET:     IN3 PIN AS OUTPUT PIN')
    GPIO.output(IN3, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN IN3 TO ', 'LOW\n')

    GPIO.setup(IN4, GPIO.OUT)
    print('\nPIN SET:     IN4 PIN AS OUTPUT PIN')
    GPIO.output(IN4, GPIO.LOW)
    print('VOLTAGE SET: OUTPUT PIN IN4 TO ', 'LOW\n')

    # INITIALIZE INPUT PINS
    GPIO.setup(STATUS_DOOR_X, GPIO.IN)
    print('\nPIN SET:     STATUS_DOOR_X PIN AS INPUT PIN')
    GPIO.setup(STATUS_SENSOR1_X, GPIO.IN)
    print('\nPIN SET:     STATUS_SENSOR1_X PIN AS INPUT PIN')
    GPIO.setup(STATUS_SENSOR2_X, GPIO.IN)
    print('\nPIN SET:     STATUS_SENSOR2_X PIN AS INPUT PIN')
    GPIO.setup(STATUS_SENSOR3_X, GPIO.IN)
    print('\nPIN SET:     STATUS_SENSOR3_X PIN AS INPUT PIN\n')

    print('\nEND___________initializePins method called___________END\n')


def setPinVoltage(pin, voltage):
    if voltage == "HIGH":
        GPIO.output(pin, GPIO.HIGH)
    else:
        GPIO.output(pin, GPIO.LOW)


def readPinVoltage(pin):
    return GPIO.input(pin)
