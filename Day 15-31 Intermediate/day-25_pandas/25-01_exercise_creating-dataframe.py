import pandas

# Create a dataframe from scratch
data_dict = {
  "students": ["Amy", "James", "John"],
  "scores": [76, 56, 69]
}

data = pandas.DataFrame(data_dict)
print(data)

# Convert the data frame to a CSV file
data.to_csv("25-01_new_data.csv")