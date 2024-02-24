import requests
from datetime import datetime

# Link to the created page: https://pixe.la/v1/users/<USERNAME>/graphs/<GRAPH_ID>.html
USERNAME = "use-your-username"
TOKEN = "use-your-token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# Create a user
user_params = {
  "token": TOKEN,
  "username": USERNAME,
  "agreeTermsOfService": "yes",
  "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Create a graph 
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
  "id": GRAPH_ID,
  "name": "Coding Graph",
  "unit": "Hours",
  "type": "float",
  "color": "ajisai",
}

headers = {
  "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# Post a pixel
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

day = datetime.now()
# day = datetime(year=2024, month=2, day=20)

pixel_config = {
  "date": day.strftime("%Y%m%d"),
  "quantity": input("How much hours did you code today? "),
}
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

# Update a pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day.strftime('%Y%m%d')}"
new_pixel_data = {
  "quantity": "2.5"
}
# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

# Delete a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{day.strftime('%Y%m%d')}"
# response = requests.delete(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)