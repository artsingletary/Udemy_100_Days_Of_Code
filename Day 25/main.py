"""
import csv

with open("data/weather_data.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)

    temperatures = []
    for row in reader:
         temperatures.append(int(row[1]))

print(temperatures)

"""

import pandas

# Load the file contents into a Panda's dataframe 
data = pandas.read_csv("data/weather_data.csv")
print(data)
print(type(data))

# Print a Panda's series
print(data["temp"])
print(type(data["temp"]))
print(data["temp"].min())
print(data["temp"].max())
print(data["temp"].mean())

# Coonvert a Panda's series to a list
data_list = data["temp"].to_list()
print(data_list)
print(type(data_list))

# Covert Panda's data dataframe to a dictionary
data_dict = data.to_dict()
print(data_dict)
print(type(data_dict))

print("Hello"[0:3])
print("Hello"[0:2])