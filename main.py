import RPi.GPIO as GPIO
import time
import datetime
import calendar
import GLCD
import AM2320
import Weather
import SW


def __main__():
    GPIO.setmode(GPIO.BCM)
    GLCD.PinsInit(20, 7, 8, 9, 18, 19, 10, 11, 12, 13, 14, 15, 16, 17)
    GLCD.GLCDInit()
    GLCD.GLCDDisplayClear()

    roop = 10 * 60 * 60
    try:
        while True:
            # if roop >= 10 * 60 * 60:
            #     Weather.RequestAPI()
            #     weather = Weather.GetWeather()
            #     temp = Weather.GetTemp()
            #     roop = 0

            # GLCD.GLCDPuts(1, 0, "Date :")
            # GLCD.GLCDPuts(10, 8, datetime.datetime.now().strftime('%Y:%m:%d %A'))
            # GLCD.GLCDPuts(1, 16, "Weather :")
            # GLCD.GLCDPuts(10,24, weather)
            # GLCD.GLCDPuts(10,32, "Temp : " + format(temp) + 'C')
            # GLCD.GLCDPuts(1, 40, "Time : " + datetime.datetime.now().strftime('%H:%M:%S'))
            # GLCD.GLCDPuts(1, 48, "Humidity    : " + AM2320.GetHum() + '%')
            # GLCD.GLCDPuts(1, 56, "Temperature : " + AM2320.GetTemp() + 'C')

            # roop += 1

            # GLCD.drowMashiro()
            SW.PinsInit(21, 22, 23, 24, 25, 26, 27)
            SW.SW_Sample()
            time.sleep(0.1)
    except KeyboardInterrupt:
        GLCD.GLCDDisplayClear()
        GPIO.cleanup()

__main__()
