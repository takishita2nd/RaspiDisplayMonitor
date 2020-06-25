import json
import urllib.request

weather = ""
temp_min = 0
temp_max = 0
temp = 0

def RequestAPI():
    global weather
    global temp_max
    global temp_min
    global temp

    url = 'http://api.openweathermap.org/data/2.5/weather?lat=&lon=&units=metric&appid='
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = json.load(res)
        weather = body['weather'][0]['main']
        temp_min = body['main']['temp_min']
        temp_max = body['main']['temp_max']
        temp = body['main']['temp']

def GetWeather():
    return weather

def GetTemp():
    return temp

def GetTempMin():
    return temp_min

def GetTempMax():
    return temp_max
