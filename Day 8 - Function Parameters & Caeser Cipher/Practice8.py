'''
#######################
### Simple Function ###
#######################

def greet():
    print("Hello Art")
    print("Nice to meet you")
    print("Hope you have a great day")

greet()

'''

'''
##############################################
### Function that allows for one parmeter  ###
##############################################
# The function below takes one parameter and the argument "Art" is passed to the  
# function

def greet(name):
     print(f"Hello {name}")
     print(f"How are you {name}?")

greet("Art")

'''

'''

####################################################
### Function that allows for multiple parameters ###
####################################################
# In the example below we are using positional arguments

def greet_with(name, location):
     print(f"Hello {name}")
     print(f"What is it like in {location}?")

greet_with("Jack Bauer", "Rome")
   
# If we wanted to use keyword arguments we would write the programe like this
# which would allow us to change the order of the arguments we are passing and still
# get the same result

def greet_with(name, location):
     print(f"Hello {name}")
     print(f"What is it like in {location}?")

greet_with(location = "Rome", name = "Jack Bauer")

'''
'''
import math

def paint_calc(height, width, cover):
    area = height * width
    number_of_cans = math.ceil((area / cover))
    print(f"Number of cans required: {number_of_cans}")
   
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc(height = test_h, width = test_w, cover = coverage)

'''
'''
# Don't include 1 because all numbers can be divided by one
def prime_checker(number):
    is_prime = True

    for i in range(2, number, 1):
        if number % i == 0:
            is_prime = False
            break

    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: ")) 
prime_checker(n)
'''

