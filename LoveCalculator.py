# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

combined_string = name1 + name2
lowercase_string = combined_string.lower()


t = combined_string.count('t')
r = combined_string.count('r')
u = combined_string.count('u')
e = combined_string.count('e')

true = t + r + u + e

l = combined_string.count('l')
o = combined_string.count('o')
v = combined_string.count('v')
e = combined_string.count('e')

love = l + o + v + e

love_score = str(true) + str(love)

print(f"Your total love score is {love_score}")

