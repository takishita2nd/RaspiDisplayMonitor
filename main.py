import RPi.GPIO as GPIO
import time
import datetime
import calendar
import GLCD
import AM2320
import Weather

sw = False

def __main__():
    global sw
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22,GPIO.IN) 
    GPIO.add_event_detect(22, GPIO.FALLING, callback=callback, bouncetime=300)
    GLCD.PinsInit(20, 7, 8, 9, 18, 19, 10, 11, 12, 13, 14, 15, 16, 17)
    GLCD.GLCDInit()
    GLCD.GLCDDisplayClear()

    roop = 10 * 60 * 60
    mode = 1
    try:
        while True:
            if sw == True:
                GLCD.GLCDDisplayClear()
                mode += 1
                if mode > 4:
                    mode = 1
                sw = False

            if mode == 1:
                if roop >= 10 * 60 * 60:
                    GLCD.GLCDDisplayClear()
                    Weather.RequestAPI()
                    weather = Weather.GetWeather()
                    temp = Weather.GetTemp()
                    roop = 0

                GLCD.GLCDPuts(1, 0, "Date :")
                GLCD.GLCDPuts(5, 8, datetime.datetime.now().strftime('%Y:%m:%d %A '))
                GLCD.GLCDPuts(1, 16, "Weather :")
                GLCD.GLCDPuts(10,24, weather)
                GLCD.GLCDPuts(10,32, "Temp : " + format(temp) + 'C')
                GLCD.GLCDPuts(1, 40, "Time : " + datetime.datetime.now().strftime('%H:%M'))
                GLCD.GLCDPuts(1, 48, "Humidity    : " + AM2320.GetHum() + '%')
                GLCD.GLCDPuts(1, 56, "Temperature : " + AM2320.GetTemp() + 'C')

                roop += 1

            elif mode == 2:
                GLCD.drowLargeClock(datetime.datetime.now().strftime('%H:%M'))
                GLCD.GLCDPuts(1, 48, "Humidity    : " + AM2320.GetHum() + '%')
                GLCD.GLCDPuts(1, 56, "Temperature : " + AM2320.GetTemp() + 'C')

            elif mode == 3:
                cal = calendar.month(datetime.datetime.now().year, datetime.datetime.now().month)
                cals = cal.split("\n")
                y = 0
                for c in cals:
                    GLCD.GLCDPuts(1, y, c)
                    y += 8
            
            elif mode == 4:
                GLCD.drowMashiro()

            time.sleep(1)
    except KeyboardInterrupt:
        GLCD.GLCDDisplayClear()
        GPIO.cleanup()

def callback(channel):
    global sw
    sw = True

__main__()
