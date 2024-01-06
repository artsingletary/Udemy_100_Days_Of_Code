numbers = [1,2,3,4]
number_list = [num + 1 for num in numbers]
print(number_list)

name = "art"
letters_list = [letter for letter in name ]
print(letters_list)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

upper_names = [name.upper() for name in names if len(name) > 5]
print(upper_names)

numbers2 = [11, 12, 13, 14]
number_list2 = [num * num for num in numbers2]
print(number_list2)

list_of_strings = input().split(',')
numbers = [int(x) for x in list_of_strings]
result = [num * num for num in numbers if num%2==0]
print(result)
