# RUN COMMAND: env FLASK_APP=app.py flask run
# Calling apis using CURL: curl -X METHOD_TYPE url

# DOOR OPENED STATUS_DOOR_X PIN VALUE = 0
# DOOR CLOSED STATUS_DOOR_X PIN VALUE = 1

# import libraries
import time
from flask import Flask
import RPi.GPIO as GPIO

# import GPIO constants & functions
from lockerActions import openDoor, checkDoorState, turnOnDoorLights, listenDoorEquipmentState, turnOffDoorLights
from gpioActions import initializePins, readPinVoltage
from multiplexorActions import setDoorSelectionMultiplexor, setDoorSensorsMultiplexor

# import general constants
from constants import durationOfDoorOpenedFeedback,  durationOfDoorWaitingToBeClosed

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')

# curl -X POST http://127.0.0.1:5000/open-door-lights/14


@app.route('/open-door-lights/<doorNumber>', methods=['POST'])
def openDoorLightsApi(doorNumber):
    print('\nAPI CALL START___________openDoorLightsApi method called___________API CALL START\n')
    turnOnDoorLights(doorNumber)
    print('\nAPI CALL END___________openDoorLightsApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'


# curl -X POST http://127.0.0.1:5000/close-door-lights/14

@app.route('/close-door-lights/<doorNumber>', methods=['POST'])
def closeDoorLightsApi(doorNumber):
    print('\nAPI CALL START___________openDoorLightsApi method called___________API CALL START\n')
    turnOffDoorLights(doorNumber)
    print('\nAPI CALL END___________openDoorLightsApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'

# curl -X POST http://127.0.0.1:5000/open-door-test/15


@app.route('/open-door-test/<doorNumber>', methods=['POST'])
def openDoorApi(doorNumber):
    print('\nAPI CALL START___________openDoor method called___________API CALL START\n')
    openDoor(doorNumber)
    print('\nAPI CALL END___________openDoor method called___________API CALL END\n')
    return f'POWER-UP FINISH'

# curl -X POST http://127.0.0.1:5000/check-door-test/15


@app.route('/check-door-test/<doorNumber>', methods=['POST'])
def checkDoorApi(doorNumber):
    print('\nAPI CALL START___________checkDoorApi method called___________API CALL START\n')
    checkDoorState(doorNumber)
    print('\nAPI CALL END___________checkDoorApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'

# curl -X POST http://127.0.0.1:5000/set-pin-high/15


@app.route('/set-pin-high/<pinNumber>', methods=['POST'])
def setPinHighApi(pinNumber):
    print('\nAPI CALL START___________setPinHighApi method called___________API CALL START\n')
    pin = int(pinNumber)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    print('set pin ', pin, 'HIGH')

    print('\nAPI CALL END___________setPinHighApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'

# curl -X POST http://127.0.0.1:5000/set-pin-low/15


@app.route('/set-pin-low/<pinNumber>', methods=['POST'])
def setPinLowApi(pinNumber):
    print('\nAPI CALL START___________setPinLowApi method called___________API CALL START\n')
    pin = int(pinNumber)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

    print('set pin ', pin, 'LOW')

    print('\nAPI CALL END___________setPinLowApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'


# curl -X POST http://127.0.0.1:5000/read-pin/15

@app.route('/read-pin/<pinNumber>', methods=['POST'])
def readPinApi(pinNumber):
    print('\nAPI CALL START___________readPinApi method called___________API CALL START\n')

    pin = int(pinNumber)
    print('pin', pin, 'state', readPinVoltage(pin))

    print('\nAPI CALL END___________readPinApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'

# curl -X POST http://127.0.0.1:5000/set-door-multiplexor/15


@app.route('/set-door-multiplexor/<doorNumber>', methods=['POST'])
def setMultiplexorApi(doorNumber):
    print('\nAPI CALL START___________readPinApi method called___________API CALL START\n')

    setDoorSelectionMultiplexor(doorNumber)
    print('\nAPI CALL END___________readPinApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'

# curl -X POST http://127.0.0.1:5000/set-sensor-multiplexor/15


@app.route('/set-sensor-multiplexor/<doorNumber>', methods=['POST'])
def setSensorMultiplexorApi(doorNumber):
    print('\nAPI CALL START___________readPinApi method called___________API CALL START\n')

    setDoorSensorsMultiplexor(doorNumber)
    print('\nAPI CALL END___________readPinApi method called___________API CALL END\n')
    return f'POWER-UP FINISH'

# EXCEPTII: Tratare cazuri cand cineva blocheaza usa!!
# POWER UP CHECKS

# Call this api using the following command: curl -X POST http://127.0.0.1:5000/power-up
# CODE VERIFIED - WORKING


@app.route('/power-up', methods=['POST'])
def powerUp():
    print('\nAPI CALL START___________power up method called___________API CALL START\n')
    initializePins()
    print('\nAPI CALL END___________power up method called___________API CALL END\n')
    return f'POWER-UP FINISH'


# START RENTAL FLOW
# 1. Open door
# 2. Listen to DOOR opened state - OPENED
# 2a. If DOOR was not OPENED OPEN DOOR.
# 2b. If DOOR was OPENED turn on the light
# 3. If DOOR was OPENED send confirmation to server with TIMESTAMP
# 4. Can DOOR be CLOSED?
# 4a. If yes Listen to DOOR opened state - CLOSED
# 4b. If no waiting for confirmation
# 5. If DOOR was CLOSED send confirmation to server with TIMESTAMP
# 6. Turn off the light.

# Call this api using the following command: curl -X POST http://127.0.0.1:5000/start-rental/doorNumber
# CODE VERIFIED - WORKING
@app.route('/start-rental/<doorNumber>', methods=['POST'])
def startRental(doorNumber):
    print('\nAPI CALL START___________startRental method called with doorNumber ',
          doorNumber, '___________API CALL START\n')

    # 1. Open door
    openDoor(doorNumber)

    # 2. Listen to DOOR opened state - OPENED
    doorState = checkDoorState(doorNumber)
    time.sleep(durationOfDoorOpenedFeedback)

    # 2a. If DOOR was not OPENED OPEN DOOR.
    if doorState == "CLOSED":
        openDoor(doorNumber)
        doorState = checkDoorState(doorNumber)
        time.sleep(durationOfDoorOpenedFeedback)

    # 2b. If DOOR was OPENED turn on the light
    if doorState == "OPENED":
        turnOnDoorLights(doorNumber)
        # 3. If DOOR was OPENED send confirmation to server with TIMESTAMP
        print("\nAPI CALL:      Send door opened confirmation to server")

    # 4. Can DOOR be CLOSED?
    # 4a. If yes Listen to DOOR opened state - CLOSED
    while doorState == "OPENED":
        doorState = checkDoorState(doorNumber)
        time.sleep(durationOfDoorOpenedFeedback)
        time.sleep(durationOfDoorWaitingToBeClosed)

    # 5. If DOOR was CLOSED send confirmation to server with TIMESTAMP
    print("\nAPI CALL:    Send door closed confirmation to server\n")
    # 6. Turn off the light.
    turnOffDoorLights(doorNumber)

    print('\nAPI CALL END___________startRental method called with doorNumber ',
          doorNumber, '___________API CALL END\n')

    return f'RENTAL HAS STARTED'

# OPEN LOCKER FLOW
# 1. Open DOOR
# 2. Listen to DOOR opened state - OPENED
# 2a. If DOOR was not OPENED OPEN DOOR.
# 2b. If DOOR was OPENED turn on the light
# 3. If DOOR was OPENED send confirmation to server with TIMESTAMP
# 4. Listen to DOOR opened state - CLOSED
# 5. If DOOR was CLOSED send confirmation to server with TIMESTAMP
# 6. Turn off the light

# Call this api using the following command: curl -X POST http://127.0.0.1:5000/open-locker/doorNumber
# CODE VERIFIED - WORKING


@app.route('/open-locker/<doorNumber>', methods=['POST'])
def openLocker(doorNumber):
    print('\nAPI CALL START___________openLocker method called with doorNumber ',
          doorNumber, '___________API CALL START\n')

    # 1. Open door
    openDoor(doorNumber)

    # 2. Listen to DOOR opened state - OPENED
    doorState = checkDoorState(doorNumber)
    time.sleep(durationOfDoorOpenedFeedback)

    # 2a. If DOOR was not OPENED OPEN DOOR.
    if doorState == "CLOSED":
        openDoor(doorNumber)
        doorState = checkDoorState(doorNumber)
        time.sleep(durationOfDoorOpenedFeedback)

    # 2b. If DOOR was OPENED turn on the light
    if doorState == "OPENED":
        turnOnDoorLights(doorNumber)
        # 3. If DOOR was OPENED send confirmation to server with TIMESTAMP
        print("\nAPI CALL:      Send door opened confirmation to server")

    # 4. Listen to DOOR opened state - CLOSED
    doorState = "OPENED"
    while doorState == "OPENED":
        doorState = checkDoorState(doorNumber)
        time.sleep(durationOfDoorOpenedFeedback)
        time.sleep(durationOfDoorWaitingToBeClosed)

    # 5. If DOOR was CLOSED send confirmation to server with TIMESTAMP
    print("\nAPI CALL:    Send door closed confirmation to server\n")
    # 6. Turn off the light.
    turnOffDoorLights(doorNumber)

    print('\nAPI CALL END___________openLocker method called with doorNumber ',
          doorNumber, '___________API CALL END\n')

    return f'DOOR WAS CLOSED'


# READ BOARD PRESENT STATE FLOW
# 1. Read BOARD present state
# 2. \nAPI CALL:    Send confirmation to server with STATE and TIMESTAMP

# Call this api using the following command: curl -X POST http://127.0.0.1:5000/read-paddle-board-state/doorNumber
# CODE VERIFIED - WORKING
@app.route('/read-paddle-board-state/<doorNumber>', methods=['POST'])
def readPaddleBoardState(doorNumber):
    print('\nSTART___________readPaddleBoardState method called with doorNumber ',
          doorNumber, '___________START\n')

    # 1. Read BOARD present state
    equipmentState = listenDoorEquipmentState(doorNumber, True)
    # 2. \nAPI CALL:      Send confirmation to server with STATE and TIMESTAMP
    print("\nAPI CALL:    Send board state confirmation to server with STATE = ", equipmentState, )

    print('\nEND___________readPaddleBoardState method called with doorNumber ',
          doorNumber, '___________END\n')

    return f'PADDLE BOARD STATE READ'


# END RENTAL FLOW
# 1. Open DOOR
# 2. Listen to DOOR opened state - OPENED
# 2a. If DOOR was not OPENED OPEN DOOR.
# 2b. If DOOR was OPENED turn on the light
# 3. If DOOR was OPENED send confirmation to server with TIMESTAMP
# 4. Can DOOR be CLOSED?
# 4a. If yes Listen to DOOR opened state - CLOSED
# 4b. If no waiting for confirmation
# 5. If DOOR was CLOSED listen to BOARD present state - PRESENT
# 6. If BOARD is not PRESENT open DOOR and return to step 5.
# 7. If BOARD is PRESENT send confirmation to server with TIMESTAMP
# 8. Turn off the light

# Call this api using the following command: curl -X POST http://127.0.0.1:5000/end-rental/doorNumber
# CODE VERIFIED - WORKING
@app.route('/end-rental/<doorNumber>', methods=['POST'])
def endRental(doorNumber):
    print('\nAPI CALL START___________endRental method called with doorNumber ',
          doorNumber, '___________API CALL START\n')

    # 1. Open door
    openDoor(doorNumber)

    # 2. Listen to DOOR opened state - OPENED
    doorState = checkDoorState(doorNumber)
    time.sleep(durationOfDoorOpenedFeedback)

    # 2a. If DOOR was not OPENED OPEN DOOR.
    if doorState == "CLOSED":
        openDoor(doorNumber)
        doorState = checkDoorState(doorNumber)
        time.sleep(durationOfDoorOpenedFeedback)

    # 2b. If DOOR was OPENED turn on the light

    if doorState == "OPENED":
        turnOnDoorLights(doorNumber)
        # 3. If DOOR was OPENED send confirmation to server with TIMESTAMP
        print("\nAPI CALL:      Send door opened confirmation to server")

    # 4. Can DOOR be CLOSED?
    # 4a. If yes Listen to DOOR opened state - CLOSED
    equipmentState = False
    while doorState == "OPENED" or equipmentState == False:
        doorState = checkDoorState(doorNumber)
        # time.sleep(durationOfDoorOpenedFeedback)
        time.sleep(durationOfDoorWaitingToBeClosed)
        # 5. If DOOR was CLOSED listen to BOARD present state - PRESENT
        if doorState == "CLOSED":
            equipmentState = listenDoorEquipmentState(doorNumber, False)
            # 6. If BOARD is not PRESENT open DOOR and return to step 5.
            if equipmentState == False:
                print("\nAPI CALL:  Send door reopened confirmation to server")
                openDoor(doorNumber)
            else:
                # 7. If BOARD is PRESENT send confirmation to server with TIMESTAMP
                # 8. Turn off the light
                print("\nAPI CALL:  Send end rental confirmation to server")
                turnOffDoorLights(doorNumber)

    print('\nAPI CALL END___________endRental method called with doorNumber ',
          doorNumber, '___________API CALL END\n')

    return f'END RENTAL'
