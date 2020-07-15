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

    SW.PinsInit(22)
    SW.Start()

    roop = 10 * 60 * 60
    mode = 1
    try:
        while True:
            key = SW.GetKey()
            if key == "ON":
                GLCD.GLCDDisplayClear()
                mode += 1
                if mode > 3:
                    mode = 1

            if mode == 1:
                if roop >= 10 * 60 * 60:
                    Weather.RequestAPI()
                    weather = Weather.GetWeather()
                    temp = Weather.GetTemp()
                    roop = 0

                GLCD.GLCDPuts(1, 0, "Date :")
                GLCD.GLCDPuts(5, 8, datetime.datetime.now().strftime('%Y:%m:%d %A'))
                GLCD.GLCDPuts(1, 16, "Weather :")
                GLCD.GLCDPuts(10,24, weather)
                GLCD.GLCDPuts(10,32, "Temp : " + format(temp) + 'C')
                GLCD.GLCDPuts(1, 40, "Time : " + datetime.datetime.now().strftime('%H:%M:%S'))
                GLCD.GLCDPuts(1, 48, "Humidity    : " + AM2320.GetHum() + '%')
                GLCD.GLCDPuts(1, 56, "Temperature : " + AM2320.GetTemp() + 'C')

                roop += 1
            elif mode == 2:
                cal = calendar.month(datetime.datetime.now().year, datetime.datetime.now().month)
                cals = cal.split("\n")
                y = 0
                for c in cals:
                    GLCD.GLCDPuts(1, y, c)
                    y += 8
            
            elif mode == 3:
                GLCD.drowMashiro()

            time.sleep(0.2)
    except KeyboardInterrupt:
        SW.Stop()
        GLCD.GLCDDisplayClear()
        GPIO.cleanup()

__main__()
