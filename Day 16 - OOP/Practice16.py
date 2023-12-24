from turtle import Turtle, Screen
import another_module

# Import the PrettyTable class
from prettytable import PrettyTable

#print(another_module.another_variable)
#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(100)

# Create a instance of the Screen Class defined in the Screen library
#my_screen = Screen()

# Print out the value of an attribute of the Screen Class
#print(my_screen.canvheight)

# Access a Screen Class method named exitonclick()
#my_screen.exitonclick()

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
