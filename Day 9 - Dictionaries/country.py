
# You can nest lists inside dictionaries, dictionaries inside dictionaries and dictionaries inside lists.
# Here we have a datastructure with a list nested inside a dictionary 
# which is itself nexted in another dictionary.

#travel_log = {
#   "France": {"cities_visited": ["Paris", "Lillie", "Dijon"], "total_visits" : 12}, 
#   "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 5},   
#}

# This function creates a new dictionary and then appends it to the travel_log list
def add_new_country(country_visited, times_visited, cities_visited):
  new_country = {}
  new_country["country"] = country_visited
  new_country["visits"] = times_visited
  new_country["cities"] = cities_visited
  
  travel_log.append(new_country)
      

# This list contains twoe dictionaries
travel_log = [
  {
   "country":"France",
   "visits": 12,
   "cities": ["Paris", "Lillie", "Dijon"]
  }, 
  {
   "country":"Germany",
   "visits": 5,
   "cities" : ["Berlin", "Hamburg", "Stuttgart"]
  },
]

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)