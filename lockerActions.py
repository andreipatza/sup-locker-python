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
    print('START___________openDoor method called with doorNumber ',
          doorNumber, '___________START')
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
    print('END___________openDoor method called with doorNumber ',
          doorNumber, '___________END')


def checkDoorState(doorNumber):
    print('START___________checkDoorState method called with doorNumber ',
          doorNumber, '___________START')
    # doorNumber type int ( 0 - 15 );

    # set multiplexor values for door with doorNumber
    setDoorSelectionMultiplexor(doorNumber)

    # Set STATUS_COMMAND = 1
    print('VOLTAGE SET: OUTPUT PIN STATUS_COMMAND TO ', 'HIGH')
    setPinVoltage(STATUS_COMMAND, "HIGH")

    # Read STATUS_DOOR_X
    # if STATUS_DOOR_X is HIGH the door is CLOSED
    # if STATUS_DOOR_X is LOW  the door is OPENED
    doorState = "OPENED" if readPinVoltage(STATUS_DOOR_X) == 0 else "CLOSED"

    # Set STATUS_COMMAND = 0
    print('VOLTAGE SET: OUTPUT PIN STATUS_COMMAND TO ', 'LOW')
    setPinVoltage(STATUS_COMMAND, "LOW")

    print('END___________checkDoorState method called with doorNumber ',
          doorNumber, '___________END')

    # return proper value
    return doorState


def turnOnDoorLights(doorNumber):
    print('START___________turnOnDoorLights method called with doorNumber ',
          doorNumber, '___________START')
    # doorNumber type int ( 0 - 15 );

    # set multiplexor values for door with doorNumber
    setDoorSelectionMultiplexor(doorNumber)

    # set multiplexor values for sensors of door with doorNumber
    setDoorSensorsMultiplexor(doorNumber)

    # Command for turning on the door lights
    # Set LED_ON_X = 1
    print('VOLTAGE SET: OUTPUT PIN LED_ON_X TO ', 'HIGH')
    setPinVoltage(LED_ON_X, "HIGH")

    print('END___________turnOnDoorLights method called with doorNumber ',
          doorNumber, '___________END')


def turnOffDoorLights(doorNumber):
    print('START___________turnOffDoorLights method called with doorNumber ',
          doorNumber, '___________START')
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

    print('END___________turnOffDoorLights method called with doorNumber ',
          doorNumber, '___________END')


def listenDoorEquipmentState(doorNumber):
    print('START___________listenDoorEquipmentState method called with doorNumber ',
          doorNumber, '___________START')
    # doorNumber type int ( 0 - 15 );

    # set multiplexor values for door with doorNumber
    setDoorSelectionMultiplexor(doorNumber)

    # set multiplexor values for sensors of door with doorNumber
    setDoorSensorsMultiplexor(doorNumber)

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

    resetDoorSensorsMultiplexor()

    if (sensor1status == "PRESENT" and sensor2status == "PRESENT" and sensor3status == "ABSENT"):
        print('END___________listenDoorEquipmentState method called with doorNumber ',
              doorNumber, 'ended with value True___________END')
        return True
    else:
        print('END___________listenDoorEquipmentState method called with doorNumber ',
              doorNumber, 'ended with value False___________END')
        return False
