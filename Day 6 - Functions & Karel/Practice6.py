class Meal:
    def __init__(self, food_item, drink, fruit=None, dessert=None):
        self.food_item = food_item
        self.drink = drink
        self.fruit = fruit
        self.dessert = dessert


class Breakfast(Meal):
    def __init__(self, food_item, drink, fruit):
        super().__init__(food_item, drink, fruit)


class Lunch(Meal):
    def __init__(self, food_item, drink):
        super().__init__(food_item, drink)


class Dinner(Meal):
    def __init__(self, food_item, drink, dessert):
        super().__init__(food_item, drink, dessert)


B1 = Breakfast("Bagel", "Juice", "Peaches")
print(f"Breakfast: {B1.food_item}, {B1.drink}, {B1.fruit}")

L1 = Lunch("Italian Sub", "Ice Tea")
print(f"Lunch: {L1.food_item}, {L1.drink}")

D1 = Dinner("Spagetti", "Coke", "Cake")
print(f"Dinner: {D1.food_item}, {D1.drink}, {D1.dessert}")

D2 = Dinner("Lasagna", "Mountain Dew", "Canoli")
print(f"Dinner: {D2.food_item}, {D2.drink}, {D2.dessert}")