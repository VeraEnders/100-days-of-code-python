import pandas

data = pandas.read_csv("2018-Central-Park-Squirrel-Census-Squirrel-Data.csv")

count_by_fur_color = data.groupby("Primary Fur Color").size()
count_by_fur_color.to_csv("25-02_squirrel-count.csv")

# # Another solution
# grey_sq_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_sq_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_sq_count = len(data[data["Primary Fur Color"] == "Black"])

# data_dict = {
#   "Fur Color": ["Gray", "Cinnamon", "Black"],
#   "Count": [grey_sq_count, red_sq_count, black_sq_count]
# }

# df = pandas.DataFrame(data_dict)
# df.to_csv("25-02_squirrel-count.csv")