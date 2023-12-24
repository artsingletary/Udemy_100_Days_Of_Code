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

# <class 'pandas.core.frame.DataFrame'>
# print(type(data))

# <class 'pandas.core.series.Series'>
data_list = data["temp"].to_list()
print(sum(data_list)/len(data_list))

print(data["temp"].mean())
print(data["temp"].max())

# Covert data dataframe to a dictionary
# data_dict = data.to_dict()
# print(data_dict)
