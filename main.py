from datetime import *
import requests

city = input("Enter the city name: ")
api = '86af77d5374b4387cfe012ec3b04ae74'

try:
    link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}'
    response = requests.get(link)
    data = response.json()

    dt = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")
    city_name = f'Weather stats for {data["name"]} || {dt}'.upper()
    weather = f'Current weather description : {data["weather"][0]["description"]}'.upper()
    temp = data["main"]["temp"] -273.15
    temperature = f'Current temperature is      : {round(temp,2)}'.upper()
    humidity = f'Current humidity            : {data["main"]["humidity"]} %'.upper()
    wind = f'Current wind speed          : {data["wind"]["speed"]} kmph'.upper()


    print("---------------------------------------------------------")
    print(city_name)
    print("---------------------------------------------------------\n")
    print(weather)
    print(temperature)
    print(humidity)
    print(wind)
    print("===============================================")

except KeyError:
    print("Invalid city name".upper())
