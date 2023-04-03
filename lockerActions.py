# import libraries
import time

# import helpers functions
from multiplexorActions import setDoorSelectionMultiplexor, setDoorSensorsMultiplexor, resetDoorSensorsMultiplexor

# import GPIO constants & functions
# OUTPUTS
from gpioActions import EN_DXX_ON, DXX_ON, IN1, IN2, IN3, IN4, LED_ON_X
# INPUTS
from gpioActions import STATUS_COMMAND, STATUS_DOOR_X, STATUS_SENSOR1_X, STATUS_SENSOR2_X, STATUS_SENSOR3_X
# FUNCTIONS
from gpioActions import setPinVoltage, readPinVoltage

# import general constants
from constants import durationOfImplse, timeBetweenImplses


def openDoor(doorNumber):
    print('\nSTART___________openDoor method called with doorNumber ',
          doorNumber, '___________START\n')
    # doorNumber type int ( 0 - 15 );

    # set multiplexor values for door with doorNumber
    setDoorSelectionMultiplexor(doorNumber)

    # Set EN_DXX_ON = 0
    # Set DXX_ON = 1
    print('VOLTAGE SET: OUTPUT PIN EN_DXX_ON TO ', 'LOW')
    setPinVoltage(EN_DXX_ON, "LOW")
    print('VOLTAGE SET: OUTPUT PIN DXX_ON TO ', 'HIGH')
    setPinVoltage(DXX_ON, "HIGH")

    # Wait durationOfImplse
    time.sleep(durationOfImplse)

    # Set DXX_ON = 0
    print('VOLTAGE SET: OUTPUT PIN DXX_ON TO ', 'LOW')
    setPinVoltage(DXX_ON, "LOW")

    # Wait timeBetweenImplses
    time.sleep(timeBetweenImplses)

    # Set DXX_ON = 1
    print('VOLTAGE SET: OUTPUT PIN DXX_ON TO ', 'HIGH')
    setPinVoltage(DXX_ON, "HIGH")

    # Wait durationOfImplse
    time.sleep(durationOfImplse)

    # Set DXX_ON = 0
    # Set EN_DXX_ON = 1
    print('VOLTAGE SET: OUTPUT PIN DXX_ON TO ', 'LOW')
    setPinVoltage(DXX_ON, "LOW")
    print('VOLTAGE SET: OUTPUT PIN EN_DXX_ON TO ', 'HIGH')
    setPinVoltage(EN_DXX_ON, "HIGH")

    # Door was opened
    print('\nEND___________openDoor method called with doorNumber ',
          doorNumber, '___________END\n')


def checkDoorState(doorNumber):
    print('\nSTART___________checkDoorState method called with doorNumber ',
          doorNumber, '___________START\n')
    # doorNumber type int ( 0 - 15 );

    # set multiplexor values for door with doorNumber
    setDoorSelectionMultiplexor(doorNumber)

    print('VOLTAGE SET: OUTPUT PIN EN_DXX_ON TO ', 'HIGH')
    setPinVoltage(EN_DXX_ON, "HIGH")

    # Read STATUS_DOOR_X
    doorState = "CLOSED" if readPinVoltage(STATUS_DOOR_X) == 0 else "OPENED"
    print('DOOR STATE IS:', doorState)

    print('VOLTAGE SET: OUTPUT PIN EN_DXX_ON TO ', 'LOW')
    setPinVoltage(EN_DXX_ON, "LOW")

    print('\nEND___________checkDoorState method called with doorNumber ',
          doorNumber, '___________END\n')

    # return proper value

    return doorState


def turnOnDoorLights(doorNumber):
    print('\nSTART___________turnOnDoorLights method called with doorNumber ',
          doorNumber, '___________START\n')
    # doorNumber type int ( 0 - 15 );

    # set multiplexor values for door with doorNumber
    setDoorSelectionMultiplexor(doorNumber)

    # set multiplexor values for sensors of door with doorNumber
    setDoorSensorsMultiplexor(doorNumber)

    # Command for turning on the door lights
    # Set LED_ON_X = 1
    print('VOLTAGE SET: OUTPUT PIN LED_ON_X TO ', 'HIGH')
    setPinVoltage(LED_ON_X, "HIGH")

    print('\nEND___________turnOnDoorLights method called with doorNumber ',
          doorNumber, '___________END\n')


def turnOffDoorLights(doorNumber):
    print('\nSTART___________turnOffDoorLights method called with doorNumber ',
          doorNumber, '___________START\n')
    # doorNumber type int ( 0 - 15 );

    # set multiplexor values for door with doorNumber
    setDoorSelectionMultiplexor(doorNumber)

    # set multiplexor values for sensors of door with doorNumber
    setDoorSensorsMultiplexor(doorNumber)

    # Command for turning on the door lights
    # Set LED_ON_X = 0
    print('VOLTAGE SET: OUTPUT PIN LED_ON_X TO ', 'LOW')
    setPinVoltage(LED_ON_X, "LOW")

    # Set IN1 = 0
    # Set IN2 = 0
    # Set IN3 = 0
    # Set IN4 = 0
    resetDoorSensorsMultiplexor()

    print('\nEND___________turnOffDoorLights method called with doorNumber ',
          doorNumber, '___________END\n')


def listenDoorEquipmentState(doorNumber, shouldResetMultiplexors):
    print('\nSTART___________listenDoorEquipmentState method called with doorNumber ',
          doorNumber, '___________START\n')
    # doorNumber type int ( 0 - 15 );

    # set multiplexor values for door with doorNumber
    setDoorSelectionMultiplexor(doorNumber)

    # set multiplexor values for sensors of door with doorNumber
    setDoorSensorsMultiplexor(doorNumber)

    time.sleep(0.1)

    # Listen to sensors state
    # Listen to STATUS_SENSOR1_X
    # Listen to STATUS_SENSOR2_X
    # Listen to STATUS_SENSOR3_X
    sensor1status = "PRESENT" if readPinVoltage(
        STATUS_SENSOR1_X) == 0 else "ABSENT"
    sensor2status = "PRESENT" if readPinVoltage(
        STATUS_SENSOR2_X) == 0 else "ABSENT"
    sensor3status = "PRESENT" if readPinVoltage(
        STATUS_SENSOR3_X) == 0 else "ABSENT"

    print('STATUS: sensor1status', sensor1status)
    print('STATUS: sensor2status', sensor2status)
    print('STATUS: sensor3status', sensor3status)

    # TODO: test time
    time.sleep(0.1)

    if shouldResetMultiplexors == True:
        resetDoorSensorsMultiplexor()

    if (sensor1status == "PRESENT" and sensor2status == "PRESENT" and sensor3status == "PRESENT"):
        print('\nEND___________listenDoorEquipmentState method called with doorNumber ',
              doorNumber, '\nENDed with value True___________END\n')
        return True
    else:
        print('\nEND___________listenDoorEquipmentState method called with doorNumber ',
              doorNumber, '\nENDed with value False___________END\n')
        return False
