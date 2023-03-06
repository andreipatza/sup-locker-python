# RUN COMMAND: env FLASK_APP=app.py flask run

# import libraries
import time
import datetime
from flask import Flask
import RPi.GPIO as GPIO

# import GPIO constants & functions
from lockerActions import openDoor, checkDoorState, turnOnDoorLights, listenDoorEquipmentState, turnOffDoorLights
from gpioActions import initializePins, STATUS_DOOR_X
from multiplexorActions import resetDoorSensorsMultiplexor

# import general constants
from constants import durationOfDoorOpenedFeedback

app = Flask(__name__)


# EXCEPTII: Tratare cazuri cand cineva blocheaza usa!!
# POWER UP CHECKS

@app.route('/power-up', methods=['POST'])
def powerUp():
    initializePins()


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
@app.route('/start-rental/<doorNumber>', methods=['POST'])
def startRental(doorNumber):
    print('START___________startRental method called with doorNumber ',
          doorNumber, '___________START')

    # 1. Open door
    openDoor(doorNumber)

    # 2. Listen to DOOR opened state - OPENED
    doorState = checkDoorState(doorNumber)

    time.sleep(durationOfDoorOpenedFeedback)

    # 2a. If DOOR was not OPENED OPEN DOOR.
    if doorState == "CLOSED":
        openDoor(doorNumber)

    # 2b. If DOOR was OPENED turn on the light
    if doorState == "OPENED":
        turnOnDoorLights(doorNumber)
        # 3. If DOOR was OPENED send confirmation to server with TIMESTAMP
        print("Send door opened confirmation to server with TIMESTAMP = ",
              datetime.datetime.now())

    # 4. Can DOOR be CLOSED?
    # 4a. If yes Listen to DOOR opened state - CLOSED
    GPIO.add_event_detect(STATUS_DOOR_X, GPIO.FALLING,
                          callback=doorClosedCallback, bouncetime=200)

    def doorClosedCallback():
        # 5. If DOOR was CLOSED send confirmation to server with TIMESTAMP
        print("Send door closed confirmation to server with TIMESTAMP = ",
              datetime.datetime.now())
        # 6. Turn off the light.
        turnOffDoorLights(doorNumber)
        GPIO.remove_event_detect(STATUS_DOOR_X)

    print('END___________startRental method called with doorNumber ',
          doorNumber, '___________END')

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


@app.route('/open-locker/<doorNumber>', methods=['POST'])
def openLocker(doorNumber):
    print('START___________openLocker method called with doorNumber ',
          doorNumber, '___________START')

    # 1. Open door
    openDoor(doorNumber)

    # 2. Listen to DOOR opened state - OPENED
    doorState = checkDoorState(doorNumber)

    time.sleep(durationOfDoorOpenedFeedback)

    # 2a. If DOOR was not OPENED OPEN DOOR.
    if doorState == "CLOSED":
        openDoor(doorNumber)

    # 2b. If DOOR was OPENED turn on the light
    if doorState == "OPENED":
        turnOnDoorLights(doorNumber)
        # 3. If DOOR was OPENED send confirmation to server with TIMESTAMP
        print("Send door opened confirmation to server with TIMESTAMP = ",
              datetime.datetime.now())

    # 4. Listen to DOOR opened state - CLOSED
    GPIO.add_event_detect(STATUS_DOOR_X, GPIO.FALLING,
                          callback=doorClosedCallback, bouncetime=200)

    def doorClosedCallback():
        # 5. If DOOR was CLOSED send confirmation to server with TIMESTAMP
        print("Send door closed confirmation to server with TIMESTAMP = ",
              datetime.datetime.now())
        # 6. Turn off the light
        turnOffDoorLights(doorNumber)
        GPIO.remove_event_detect(STATUS_DOOR_X)

    print('END___________openLocker method called with doorNumber ',
          doorNumber, '___________END')

    return f'DOOR WAS CLOSED'


# READ BOARD PRESENT STATE FLOW
# 1. Read BOARD present state
# 2. Send confirmation to server with STATE and TIMESTAMP
@app.route('/read-paddle-board-state/<doorNumber>', methods=['POST'])
def readPaddleBoardState(doorNumber):
    print('START___________readPaddleBoardState method called with doorNumber ',
          doorNumber, '___________START')

    # 1. Read BOARD present state
    equipmentState = listenDoorEquipmentState(doorNumber)
    # 2. Send confirmation to server with STATE and TIMESTAMP
    print("Send board state confirmation to server with STATE = ", equipmentState, " and TIMESTAMP = ",
          datetime.datetime.now())

    print('END___________readPaddleBoardState method called with doorNumber ',
          doorNumber, '___________END')

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
@app.route('/end-rental/<doorNumber>', methods=['POST'])
def endRental(doorNumber):
    print('START___________endRental method called with doorNumber ',
          doorNumber, '___________START')

    # 1. Open door
    openDoor(doorNumber)

    # 2. Listen to DOOR opened state - OPENED
    doorState = checkDoorState(doorNumber)

    time.sleep(durationOfDoorOpenedFeedback)

    # 2a. If DOOR was not OPENED OPEN DOOR.
    if doorState == "CLOSED":
        openDoor(doorNumber)

    # 2b. If DOOR was OPENED turn on the light
    if doorState == "OPENED":
        turnOnDoorLights(doorNumber)
        # 3. If DOOR was OPENED send confirmation to server with TIMESTAMP
        print("Send door opened confirmation to server with TIMESTAMP = ",
              datetime.datetime.now())

    # 4. Can DOOR be CLOSED?
    # 4a. If yes Listen to DOOR opened state - CLOSED
    GPIO.add_event_detect(STATUS_DOOR_X, GPIO.FALLING,
                          callback=doorClosedCallback, bouncetime=200)

    def doorClosedCallback():
        # 5. If DOOR was CLOSED listen to BOARD present state - PRESENT
        equipmentState = listenDoorEquipmentState(doorNumber)
        if equipmentState == False:
            # 6. If BOARD is not PRESENT open DOOR and return to step 5.
            print("Send door reopened confirmation to server with TIMESTAMP = ",
                  datetime.datetime.now())
            openDoor(doorNumber)
        else:
            # 7. If BOARD is PRESENT send confirmation to server with TIMESTAMP
            # 8. Turn off the light
            print("Send door closed confirmation to server with TIMESTAMP = ",
                  datetime.datetime.now())
            turnOffDoorLights(doorNumber)
            GPIO.remove_event_detect(STATUS_DOOR_X)

    print('END___________endRental method called with doorNumber ',
          doorNumber, '___________END')
