import requests
import datetime as dt

# Find lat long coordinates using the name of a place, city, state, or address- https://www.latlong.net/
# City = Paris
MY_LAT = 48.856613
MY_LONG = 2.352222

parameters = {
  "lat": MY_LAT,
  "lng": MY_LONG,
  "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise, sunset)

now = dt.datetime.now()
print(now.hour)
