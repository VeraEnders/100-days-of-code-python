# Nesting
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel_log = {
  "France": ["Paris", "Lille"],
  "Germany": ["Berlin", "Hamburg"],
}

# Nesting dictionary in a dictionary
travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille"], 
    "total_visits": 12
  },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg"], 
    "total_visits": 5
  },
}

# Nesting dictionary in a list
travel_log = [
  {
    "country": "France",
    "cities_visited": ["Paris", "Lille"], 
    "total_visits": 12
  },
  {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg"], 
    "total_visits": 5
  },
]