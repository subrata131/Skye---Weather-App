import streamlit as s
import requests
import os
s.markdown("""
<style>
body {
    background-color:#0e1117;
    color:black;
}
.stTextInput input {
    border-radius:10px;
}
div[data-testid="stButton"] button {
    border-radius:10px;
    background-color:#4CAF50;
    color:white;
}
</style>
""", unsafe_allow_html=True)
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv("API_KEY")
s.set_page_config(layout="wide")
s.markdown("<h1 style='text-align:center;'>🌦 Skye</h1>", unsafe_allow_html=True)

#s.set_page_config(page_title="Skye",page_icon="🌦",layout="centered")
#s.markdown("<h1 style='text-align:center';> Skye <h/h1>",unsafe_allow_html=True)
s.markdown("<p style='text-align: center;'>Real-Time Weather + Forecast</p>",unsafe_allow_html=True)
s.divider()

# s.title("Skye")
# s.subheader("🌦 Weather prediction App")
# s.subheader("Get Real-Time Weather Data ")
city=s.text_input("Enter city name")
if s.button("Get Weather"):
    if city=="":
        s.warning("!! Please Enter a city name")
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        with s.spinner("Fatching Weather...."):
            
             response=requests.get(url)
             data= response.json()
        if str(data["cod"])== "200":
            temp=data["main"]["temp"]
            humidity=data["main"]["humidity"]
            pressure=data["main"]["pressure"]
            weather= data["weather"][0]["description"]
            icon=data["weather"][0]["icon"]
            icon_url=f"http://openweathermap.org/img/wn/{icon}@2x.png"
            s.markdown("## Current Weather")
            s.divider()

            col1,col2 = s.columns(2)
            with col1:
                s.image(icon_url)
            with col2:
                
                s.markdown(f"""
<div style="
    background-color:#1c1f26;
    padding:25px;
    border-radius:15px;
    color:white;
    box-shadow:0px 4px 12px rgba(0,0,0,0.4);
">
    <h2 style="color:#4CAF50;">🌡 {temp}°C</h2>
    <p style="font-size:16px;">💧 Humidity: {humidity}%</p>
    <p style="font-size:16px;">🌥 Condition: {weather}</p>
    <p style="font-size:16px;">ضغط Pressure: {pressure} hPa</p>
</div>
""", unsafe_allow_html=True)
                

            s.divider()

            forecast=f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"
            forecast_data=requests.get(forecast).json()
            s.subheader(" 5-Day Forecast")
            col=s.columns(3)
            for i in range(5):

                day= forecast_data["list"][i*8]
                cols=col[i%3]


            # for i in range(0,40,8):
            #     day=forecast_data["list"][i]


                from datetime import datetime
                date_raw= day["dt_txt"]
                date=datetime.strptime(date_raw, "%Y-%m-%d %H:%M:%S")
                date = date.strftime("%a, %d %B")

                temp=day["main"]["temp"]
                desc=day["weather"][0]["description"]
                icon=day["weather"][0]["icon"]
                icon_url=f"http://openweathermap.org/img/wn/{icon}.png"
                # col1,col2=s.columns([1,2])
                # with col1:
                #     s.image(icon_url)
                # with col2:
                #     s.write(f" {date}")
                #     s.write(f" {temp}")
                #     s.write(f" {desc}")
                # s.divider()
                with cols:


                       s.markdown(f"""<div style="
                           background-color:#f0f2f6;
                           padding:15px;
                           border-radius:10px;
                           margin-bottom:10px;
                           ">
                           <h4>{date}</h4>
                           <img src="{icon_url}">
                           <p> {temp}°C</p>
                           <p> {desc}</p>
                           </div>
                           """,unsafe_allow_html=True
                           )
        




            # s.success(f" Temerature:{temp}°C")
            # s.info(f"Humidity:{humidity}%")
            # s.write(f"Condition:{weather}")
            # s.write(f"Pressure:{pressure} hPa")
        else:
            s.error("City not found")