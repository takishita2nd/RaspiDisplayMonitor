import os
import sys
import urllib.parse
import json
import RPi.GPIO as GPIO
import time
import datetime
import calendar
import GLCD
import AM2320
import Weather
import threading

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from http import HTTPStatus

PORT = 8000
sw = False

Humidity = 0
Temperature = 0

def __main__():
    global sw
    global Humidity
    global Temperature

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(22,GPIO.IN) 
    GPIO.add_event_detect(22, GPIO.FALLING, callback=callback, bouncetime=300)
    GLCD.PinsInit(20, 7, 8, 9, 18, 19, 10, 11, 12, 13, 14, 15, 16, 17)
    GLCD.GLCDInit()
    GLCD.GLCDDisplayClear()

    roop = 10 * 60 * 60
    mode = 1
    
    thread = threading.Thread(target=httpServe)
    thread.start()
    
    try:
        while True:
            Humidity = AM2320.GetHum()
            Temperature = AM2320.GetTemp()

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
                GLCD.GLCDPuts(1, 48, "Humidity    : " + Humidity + '%')
                GLCD.GLCDPuts(1, 56, "Temperature : " + Temperature + 'C')

                roop += 1

            elif mode == 2:
                GLCD.drowLargeClock(datetime.datetime.now().strftime('%H:%M'))
                GLCD.GLCDPuts(1, 48, "Humidity    : " + Humidity + '%')
                GLCD.GLCDPuts(1, 56, "Temperature : " + Temperature + 'C')

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

def httpServe():
    handler = StubHttpRequestHandler
    httpd = HTTPServer(('',PORT),handler)
    httpd.serve_forever()

class StubHttpRequestHandler(BaseHTTPRequestHandler):
    server_version = "HTTP Stub/0.1"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_GET(self):
        enc = sys.getfilesystemencoding()

        data = {
            'datetime' : datetime.datetime.now().strftime('%Y:%m:%d %H:%M:%S'),
            'temperature': Temperature,
            'humidity': Humidity,
        }

        encoded = json.dumps(data).encode()

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/html; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded)))
        self.end_headers()

        self.wfile.write(encoded)     

__main__()
