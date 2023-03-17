from gpioActions import setPinVoltage
from gpioActions import S0, S1, S2, S3, IN1, IN2, IN3, IN4


def setDoorSelectionMultiplexor(doorNumber):
    print('\nSTART___________setDoorSelectionMultiplexor method called with doorNumber ',
          doorNumber, '___________START\n')
    # doorNumber type int ( 0 - 15 );

    # convert doorNumber from integer to binary
    doorNumberBinary = format(int(doorNumber), '04b')

    # get binary array
    convertedBinaryArray = [int(x) for x in doorNumberBinary]

    # calculate values for multiplexor
    S3value = "HIGH" if convertedBinaryArray[3] == 1 else "LOW"
    S2value = "HIGH" if convertedBinaryArray[2] == 1 else "LOW"
    S1value = "HIGH" if convertedBinaryArray[1] == 1 else "LOW"
    S0value = "HIGH" if convertedBinaryArray[0] == 1 else "LOW"

    # set voltage levels for multiplexor
    print('VOLTAGE SET: OUTPUT PIN S0 TO ', S0value)
    setPinVoltage(S0, S0value)
    print('VOLTAGE SET: OUTPUT PIN S1 TO ', S1value)
    setPinVoltage(S1, S1value)
    print('VOLTAGE SET: OUTPUT PIN S2 TO ', S2value)
    setPinVoltage(S2, S2value)
    print('VOLTAGE SET: OUTPUT PIN S3 TO ', S3value)
    setPinVoltage(S3, S3value)

    print('\nEND___________setDoorSelectionMultiplexor method called with doorNumber ',
          doorNumber, '___________END\n')


def setDoorSensorsMultiplexor(doorNumber):
    print('\nSTART___________setDoorSensorsMultiplexor method called with doorNumber ',
          doorNumber, '___________START\n')
    # doorNumber type int ( 0 - 15 )

    doorNumber = int(doorNumber)

    # If doorNumber between 0 - 3
    # Set IN1 = 1
    if 0 <= doorNumber <= 3:
        print('VOLTAGE SET: OUTPUT PIN IN1 TO ', 'HIGH')
        setPinVoltage(IN1, "HIGH")

    # If doorNumber between 4 - 7
    # Set IN2 = 1
    if 4 <= doorNumber <= 7:
        print('VOLTAGE SET: OUTPUT PIN IN2 TO ', 'HIGH')
        setPinVoltage(IN2, "HIGH")

    # If doorNumber between 8 - 11
    # Set IN3 = 1
    if 8 <= doorNumber <= 11:
        print('VOLTAGE SET: OUTPUT PIN IN3 TO ', 'HIGH')
        setPinVoltage(IN3, "HIGH")

    # If doorNumber between 12 - 15
    # Set IN4 = 1
    if 12 <= doorNumber <= 15:
        print('VOLTAGE SET: OUTPUT PIN IN4 TO ', 'HIGH')
        setPinVoltage(IN4, "HIGH")

    print('\nEND___________setDoorSensorsMultiplexor method called with doorNumber ',
          doorNumber, '___________END\n')


def resetDoorSensorsMultiplexor():
    print('\nSTART___________resetDoorSensorsMultiplexor method called___________START\n')
    print('VOLTAGE SET: OUTPUT PIN IN1 TO ', 'LOW')
    setPinVoltage(IN1, "LOW")
    print('VOLTAGE SET: OUTPUT PIN IN2 TO ', 'LOW')
    setPinVoltage(IN2, "LOW")
    print('VOLTAGE SET: OUTPUT PIN IN3 TO ', 'LOW')
    setPinVoltage(IN3, "LOW")
    print('VOLTAGE SET: OUTPUT PIN IN4 TO ', 'LOW')
    setPinVoltage(IN4, "LOW")
    print('\nEND___________resetDoorSensorsMultiplexor method called___________END\n')
