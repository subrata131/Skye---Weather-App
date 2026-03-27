import requests
import os

from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("API_KEY")
def get(city):
    url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    data=requests.get(url).json()

    if data["cod"]==200:
        print("\n... CURRENT WEATHER....")
        print("City:",city)
        print("Temperature:",data["main"]["temp"],"C")
        print("Humidity:",data["main"]["humidity"],"%")
        print("Condition:",data["weather"][0]["description"])
    else:
        print("City not found")

def forecast(city):
    url=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
    data=requests.get(url).json()

    print("\n....5-DAY FORECAST...")
    for i in range(0,40,8):
        day= data["list"][i]
        print("\nDate:",day["dt_txt"])
        print("Temp:",day["main"]["temp"],"C")
        print("Humidity:",day["main"]["humidity"],"%")
        print("Condition:",day["weather"][0]["description"])

while True:
    print("\n...SKYE WEATHER....")
    print("1.Get Weather\n2.Exit")
    ch=int(input("Enter your choice:"))
    if ch==1:
        city=input("Enter city name:")
        get(city)
        forecast(city)
    elif ch==2:
        print("Exiting...")
        break
    else:
        print("Invalid input")


        