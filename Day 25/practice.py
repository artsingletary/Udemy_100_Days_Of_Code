import pandas
"""
data = pandas.read_csv("data/weather_data.csv")

# Load the file contents into a Panda's dataframe 
print(data)
print(type(data))

# Print a Panda's series

# Here we are treating the data frame almost like a dictionary
# and you are pulling out each column by the key.
print(data["temp"])

# Here you are treating the dataframe like and object
print(data.temp)


print(type(data["temp"]))
print(data["temp"].min())
print(data["temp"].max())
print(data["temp"].mean())

# Print the character at the 4 index
print("Hello"[4])
# Print the characters at the 0, 1 and 2 index
print("Hello"[0:3])
# Reverse a string
print("Hello"[::-1])

# Print the row where the day column is equal to Monday
print(data[data.day == "Monday"])

# Print the row where the temperature is the maximum
print(data[data.temp == data.temp.max()])

# Coonvert a Panda's series to a list
data_list = data["temp"].to_list()
print(data_list)
print(type(data_list))

# Covert Panda's data dataframe to a dictionary
data_dict = data.to_dict()
print(data_dict)
print(type(data_dict))
"""


# Create a dataframe from scratch
data_dict = {
     "students": ["Art", "Kristen", "Justin"],
     "scores": [76, 56, 65]
}

#Create the pandas dataframe
data = pandas.DataFrame(data_dict)
print(data)

#Convert the pandas dataframe to a CSV
data.to_csv("data/new_data.csv")