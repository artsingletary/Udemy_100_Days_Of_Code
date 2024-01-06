import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# Get the response code.  If there is a problem you will receive the response code of the error
response.raise_for_status()

# Get the coordinates
coordinates = response.json()["iss_position"]
print(coordinates)

# Get the longitude
longitude = response.json()["iss_position"]["longitude"]

# Get the latitude
latitude = response.json()["iss_position"]["latitude"]

# Place information in a tuple
iss_position = (longitude, latitude)

# Print the tuple
print(iss_position)


