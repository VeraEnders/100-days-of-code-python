# with open("weather-data.csv") as file:
#   data = file.readlines()
#   print(data)

# import csv
# with open("weather-data.csv") as file:
#   data = csv.reader(file)
#   temperatures = []
#   for row in data:
#     if row[1] != "temp":
#       temperatures.append(int(row[1]))
#   print(temperatures)

import pandas
data = pandas.read_csv("weather-data.csv")
# print(data["temp"])

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(len(temp_list)) 
print(temp_list) 

# Find an average temperature
avg_temp_1 = sum(temp_list) / len(temp_list)
print(avg_temp_1)
# or
avg_temp_2 = data["temp"].mean()
print(avg_temp_2)

# Get Data in Columns
# data.condition
print(data["condition"])

# Which row of data had the highest temperature in the week
max_temp = data["temp"].max()
row_highest_temp = data[data["temp"] == max_temp]
print(row_highest_temp)

# Get Data in Row
monday = data[data["day"] == "Monday"]
print(monday)

# Monday temperature in F
monday_temp = int(monday.temp)
monday_temp_in_F = monday_temp * 9/5 + 32
print(monday_temp_in_F)