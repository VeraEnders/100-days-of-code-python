# Dictionary in List

# Write a program that adds to a travel_log. 
# You can see a travel_log which is a List that contains 2 Dictionaries.
# DO NOT modify the travel_log directly. You need to create a function that modifies it.

travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]

def add_new_country(name_country, total_visits, names_cities):
  new_country = {
    "country": name_country,
    "visits": total_visits,
    "cities": names_cities
  }
  travel_log.append(new_country)

add_new_country("Australia", 2, ["Bunbury", "Sydney"])
print(travel_log)