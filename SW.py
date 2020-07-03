import RPi.GPIO as GPIO
import time

X_p = 0
Y_p = 0
Z_p = 0
A_p = 0
B_p = 0
C_p = 0
D_p = 0

def PinsInit(x, y, z, a, b, c, d):
    global X_p
    global Y_p
    global Z_p
    global A_p
    global B_p
    global C_p
    global D_p

    X_p = x
    Y_p = y
    Z_p = z
    A_p = a
    B_p = b
    C_p = c
    D_p = d

    GPIO.setup(X_p, GPIO.OUT)
    GPIO.setup(Y_p, GPIO.OUT)
    GPIO.setup(Z_p, GPIO.OUT)
    GPIO.setup(A_p, GPIO.IN)
    GPIO.setup(B_p, GPIO.IN)
    GPIO.setup(C_p, GPIO.IN)
    GPIO.setup(D_p, GPIO.IN)

    GPIO.output(X_p, GPIO.HIGH)
    GPIO.output(Y_p, GPIO.HIGH)
    GPIO.output(Z_p, GPIO.HIGH)

def SW_Sample():
    col = 1
    aStore = 1
    bStore = 1
    cStore = 1
    dStore = 1
    colStore = 0
    while True:
        if col == 1:
            GPIO.output(X_p, GPIO.LOW)
            GPIO.output(Y_p, GPIO.HIGH)
            GPIO.output(Z_p, GPIO.HIGH)
        elif col == 2:
            GPIO.output(X_p, GPIO.HIGH)
            GPIO.output(Y_p, GPIO.LOW)
            GPIO.output(Z_p, GPIO.HIGH)
        else:
            GPIO.output(X_p, GPIO.HIGH)
            GPIO.output(Y_p, GPIO.HIGH)
            GPIO.output(Z_p, GPIO.LOW)
        if dStore == 1 and GPIO.input(D_p) == 0:
            time.sleep(0.05)
            if GPIO.input(D_p) == 0:
                if col == 1 and colStore == 0:
                    print("push 1")
                    colStore = 1
                elif col == 2 and colStore == 0:
                    print("push 2")
                    colStore = 2
                elif col == 3 and colStore == 0:
                    print("push 3")
                    colStore = 3
                dStore = 0
        elif dStore == 0 and GPIO.input(D_p) == 1:
            if col == 1 and colStore == 1:
                print("release 1")
                colStore = 0
                dStore = 1
            elif col == 2 and colStore == 2:
                print("release 2")
                colStore = 0
                dStore = 1
            elif col == 3 and colStore == 3:
                print("release 3")
                colStore = 0
                dStore = 1
        elif cStore == 1 and GPIO.input(C_p) == 0:
            time.sleep(0.05)
            if GPIO.input(C_p) == 0:
                if col == 1 and colStore == 0:
                    print("push 4")
                    colStore = 1
                elif col == 2 and colStore == 0:
                    print("push 5")
                    colStore = 2
                elif col == 3 and colStore == 0:
                    print("push 6")
                    colStore = 3
                cStore = 0
        elif cStore == 0 and GPIO.input(C_p) == 1:
            if col == 1 and colStore == 1:
                print("release 4")
                colStore = 0
                cStore = 1
            elif col == 2 and colStore == 2:
                print("release 5")
                colStore = 0
                cStore = 1
            elif col == 3 and colStore == 3:
                print("release 6")
                colStore = 0
                cStore = 1
        elif bStore == 1 and GPIO.input(B_p) == 0:
            time.sleep(0.05)
            if GPIO.input(B_p) == 0:
                if col == 1 and colStore == 0:
                    print("push 7")
                    colStore = 1
                elif col == 2 and colStore == 0:
                    print("push 8")
                    colStore = 2
                elif col == 3 and colStore == 0:
                    print("push 9")
                    colStore = 3
                bStore = 0
        elif bStore == 0 and GPIO.input(B_p) == 1:
            if col == 1 and colStore == 1:
                print("release 7")
                colStore = 0
                bStore = 1
            elif col == 2 and colStore == 2:
                print("release 8")
                colStore = 0
                bStore = 1
            elif col == 3 and colStore == 3:
                print("release 9")
                colStore = 0
                bStore = 1
        elif aStore == 1 and GPIO.input(A_p) == 0:
            time.sleep(0.05)
            if GPIO.input(A_p) == 0:
                if col == 1 and colStore == 0:
                    print("push *")
                    colStore = 1
                elif col == 2 and colStore == 0:
                    print("push 0")
                    colStore = 2
                elif col == 3 and colStore == 0:
                    print("push #")
                    colStore = 3
                aStore = 0
        elif aStore == 0 and GPIO.input(A_p) == 1:
            if col == 1 and colStore == 1:
                print("release *")
                colStore = 0
                aStore = 1
            elif col == 2 and colStore == 2:
                print("release 0")
                colStore = 0
                aStore = 1
            elif col == 3 and colStore == 3:
                print("release #")
                colStore = 0
                aStore = 1

        col += 1
        if col > 3:
            col = 1
