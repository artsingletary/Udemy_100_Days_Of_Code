import os

def clear():
  os.system('cls')

# Declare a bids dictionary
bids = {}

while True:
    clear()
    name = input("What is your name?: ")
    amount = int(input("What is your bid?: "))
    continue_auction = input("Are there other bids?: ")

    # Add entry to the bids dictionary
    bids[name] = amount


    if (continue_auction == "yes"):
      continue
    elif (continue_auction == "no"): 
      break
    else:
      print("Invalid selection\n")
      continue

# Print the contents of the bids dictionary
print(bids)