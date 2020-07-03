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
    swState = [0] * 12
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

        # 1押下
        if swState[1] == 0 and col == 1 and GPIO.input(D_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(D_p) == 0:
                print("push 1")
                swState[1] = 1
        # 1押下戻し
        elif swState[1] == 1 and col == 1 and GPIO.input(D_p) == 1:
            print("release 1")
            swState[1] = 0
        # 2押下
        if swState[2] == 0 and col == 2 and GPIO.input(D_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(D_p) == 0:
                print("push 2")
                swState[2] = 1
        # 2押下戻し
        elif swState[2] == 1 and col == 2 and GPIO.input(D_p) == 1:
            print("release 2")
            swState[2] = 0
        # 3押下
        if swState[3] == 0 and col == 3 and GPIO.input(D_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(D_p) == 0:
                print("push 3")
                swState[3] = 1
        # 3押下戻し
        elif swState[3] == 1 and col == 3 and GPIO.input(D_p) == 1:
            print("release 3")
            swState[3] = 0
        # 4押下
        if swState[4] == 0 and col == 1 and GPIO.input(C_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(C_p) == 0:
                print("push 4")
                swState[4] = 1
        # 4押下戻し
        elif swState[4] == 1 and col == 1 and GPIO.input(C_p) == 1:
            print("release 4")
            swState[4] = 0
        # 5押下
        if swState[5] == 0 and col == 2 and GPIO.input(C_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(C_p) == 0:
                print("push 5")
                swState[5] = 1
        # 5押下戻し
        elif swState[5] == 1 and col == 2 and GPIO.input(C_p) == 1:
            print("release 5")
            swState[5] = 0
        # 6押下
        if swState[6] == 0 and col == 3 and GPIO.input(C_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(C_p) == 0:
                print("push 6")
                swState[6] = 1
        # 6押下戻し
        elif swState[6] == 1 and col == 3 and GPIO.input(C_p) == 1:
            print("release 6")
            swState[6] = 0
        # 7押下
        if swState[7] == 0 and col == 1 and GPIO.input(B_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(B_p) == 0:
                print("push 7")
                swState[7] = 1
        # 7押下戻し
        elif swState[7] == 1 and col == 1 and GPIO.input(B_p) == 1:
            print("release 7")
            swState[7] = 0
        # 8押下
        if swState[8] == 0 and col == 2 and GPIO.input(B_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(B_p) == 0:
                print("push 8")
                swState[8] = 1
        # 8押下戻し
        elif swState[8] == 1 and col == 2 and GPIO.input(B_p) == 1:
            print("release 8")
            swState[8] = 0
        # 9押下
        if swState[9] == 0 and col == 3 and GPIO.input(B_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(B_p) == 0:
                print("push 9")
                swState[9] = 1
        # 9押下戻し
        elif swState[9] == 1 and col == 3 and GPIO.input(B_p) == 1:
            print("release 9")
            swState[9] = 0
        # *押下
        if swState[10] == 0 and col == 1 and GPIO.input(A_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(A_p) == 0:
                print("push *")
                swState[10] = 1
        # *押下戻し
        elif swState[10] == 1 and col == 1 and GPIO.input(A_p) == 1:
            print("release *")
            swState[10] = 0
        # 0押下
        if swState[0] == 0 and col == 2 and GPIO.input(A_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(A_p) == 0:
                print("push 0")
                swState[0] = 1
        # 0押下戻し
        elif swState[0] == 1 and col == 2 and GPIO.input(A_p) == 1:
            print("release 0")
            swState[0] = 0
        # #押下
        if swState[11] == 0 and col == 3 and GPIO.input(A_p) == 0:
            # チャタリング回避
            time.sleep(0.05)
            if GPIO.input(A_p) == 0:
                print("push #")
                swState[11] = 1
        # #押下戻し
        elif swState[11] == 1 and col == 3 and GPIO.input(A_p) == 1:
            print("release #")
            swState[11] = 0

        col += 1
        if col > 3:
            col = 1
