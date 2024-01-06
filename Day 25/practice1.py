import pandas
data = pandas.read_csv("data/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# Count the number of rows that contain gray squirrels
gray_count = (len(data[data["Primary Fur Color"] == "Gray"]))

# Count the number of rows that contain cinnamon squirrels
cinnamon_count = (len(data[data["Primary Fur Color"] == "Cinnamon"]))

# Count the number of rows that contain black squirrels
black_count = (len(data[data["Primary Fur Color"] == "Black"]))


# Create a dataframe from scratch
data_dict = {
     "Fur Color": ["Gray", "Cinnamon", "Black"],
     "Count": [gray_count, cinnamon_count, black_count]
}

#Create the pandas dataframe
data = pandas.DataFrame(data_dict)

#Convert the pandas dataframe to a CSV
data.to_csv("data/squirrel_count.csv")