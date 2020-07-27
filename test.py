import RPi.GPIO as GPIO
import GLCD
import LFont

def __main__():
    GPIO.setmode(GPIO.BCM)
    GLCD.PinsInit(20, 7, 8, 9, 18, 19, 10, 11, 12, 13, 14, 15, 16, 17)
    GLCD.GLCDInit()
    GLCD.GLCDDisplayClear()
    try:
        while True:
            for page in range(6):
                for addr in range(24):
                    GLCD.SelectIC(1)
                    GLCD.SetPage(page)
                    GLCD.SetAddress(addr)
                    GLCD.WriteData(LFont.Array[5][page][addr])
            for page in range(6):
                for addr in range(24):
                    GLCD.SelectIC(1)
                    GLCD.SetPage(page)
                    GLCD.SetAddress(addr + 24)
                    GLCD.WriteData(LFont.Array[6][page][addr])
            for page in range(6):
                for addr in range(24):
                    if addr < 16:
                        GLCD.SelectIC(1)
                        GLCD.SetPage(page)
                        GLCD.SetAddress(addr + 48)
                    else:
                        GLCD.SelectIC(2)
                        GLCD.SetPage(page)
                        GLCD.SetAddress(addr - 16)
                    GLCD.WriteData(LFont.Array[10][page][addr])
            for page in range(6):
                for addr in range(24):
                    GLCD.SelectIC(2)
                    GLCD.SetPage(page)
                    GLCD.SetAddress(addr + 8)
                    GLCD.WriteData(LFont.Array[8][page][addr])
            for page in range(6):
                for addr in range(24):
                    GLCD.SelectIC(2)
                    GLCD.SetPage(page)
                    GLCD.SetAddress(addr + 32)
                    GLCD.WriteData(LFont.Array[9][page][addr])

    except KeyboardInterrupt:
        GLCD.GLCDDisplayClear()
        GPIO.cleanup()

__main__()
