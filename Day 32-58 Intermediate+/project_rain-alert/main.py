import requests
import smtplib
import os

MY_EMAIL = "sender-name@gmail.com"
# Gmail app password 
PASSWORD = "qwerty"

# OpenWeatherMap
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = os.environ.get("OWM_API_KEY")

LAT = 52.259319
LON = -7.110070

def send_email():
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
      from_addr=MY_EMAIL, 
      to_addrs=f"{MY_EMAIL}", 
      msg=f"It's raining!\n\nBring an umbrella."
    )

parameters = {
  "lat": LAT,
  "lon": LON,
  "appid": API_KEY,
}

response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()

data = response.json()

weather_code = data["weather"][0]["id"]
if weather_code < 700:
  send_email()
  print("Bring an umbrella.")
