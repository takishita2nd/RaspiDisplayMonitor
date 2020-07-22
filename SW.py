import RPi.GPIO as GPIO
import time
import threading

A_p = 0

Non = ""
Key = Non

thread = None
Loop = True

def PinsInit(a):
    global A_p
    A_p = a
    GPIO.setup(A_p, GPIO.IN)

def Start():
    thread = threading.Thread(target=threadProcess)
    thread.start()

def Stop():
    global Loop
    Loop = False

def GetKey():
    global Key
    ret = Key
    Key = Non
    return ret

def threadProcess():
    global Key

    swState = [0]
    while Loop:

        if swState[0] == 0 and GPIO.input(A_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(A_p) == 0:
                Key = "ON"
                swState[0] = 1
        elif swState[0] == 1 and GPIO.input(A_p) == 1:
            Key = Non
            swState[0] = 0

        time.sleep(0.2)
