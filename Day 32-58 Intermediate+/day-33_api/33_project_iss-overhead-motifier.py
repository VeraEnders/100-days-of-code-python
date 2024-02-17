import requests
import datetime as dt
import smtplib
import time

# Task
# Create a program that send an email
# if the ISS is overhead and it is currently nighttime

# Requests is a simple HTTP library for Python
# https://requests.readthedocs.io/en/latest/user/quickstart/#errors-and-exceptions

# My City = Paris
MY_LAT = 48.856613
MY_LONG = 2.352222

MY_EMAIL = "sender-name@gmail.com"
# Gmail app password 
PASSWORD = "qwerty"

def is_iss_overhead():
  """Checks if the ISS is overhead"""
  # Make a Request
  response = requests.get(url="http://api.open-notify.org/iss-now.json")

  # Handle exceptions
  response.raise_for_status()

  # JSON Response Content
  data = response.json()

  # Get ISS latitude and longitude
  iss_latitude = float(data["iss_position"]["latitude"])
  iss_longitude = float(data["iss_position"]["longitude"])

  # Check if my position is within +5 or -5 degrees of the ISS position
  if (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5):
    return True


def is_night():
  """Checks if it is currently nighttime"""
  parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
  }

  response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
  response.raise_for_status()

  data = response.json()
  sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
  sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

  time_now = dt.datetime.now()
  if time_now >= sunset or time_now <= sunrise:
    return True

# Sending an email
while True:
  time.sleep(60)

  if is_iss_overhead and is_night:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.sendmail(
      from_addr=MY_EMAIL,
      to_addrs=MY_EMAIL,
      msg="Subject:Look Up!\n\nThe ISS is above you in the sky."
    )
