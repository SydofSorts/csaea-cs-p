# # USER INPUT IN PYTHON
# # print("<PROMPT>")

# name = input("Enter your name: ")
# print(f"Hello {name}!")

# print(type(name))

# age = input("Enter your age: ")
# print(f"Your age is {age}!")

# print(type(age))

# age_converted = int(age)
# print(type(age_converted))

# height = float(input("Enter your height in meters: "))
# print(f"You are {height} meters tall")
# print(height + 1)

# Challenge 1: Favorite Color
color = input("Enter your favorite color: ")
print(f"Your favorite color is {color}")

# Challenge 2: Adding Two Numbers

num1 = float(input("Enter any number: "))
num2 = float(input("Enter another number of your choosing: "))
sum_total = num1 + num2
print(f"The sum of your two chosen numbers is {sum_total}!")

# Challenge 3: Circle Area from User Input

import math

diameter = float(input("Enter diameter for circle: "))
radius = diameter * 0.5
circle_area = math.pi * math.pow(radius, 2)
print(f"The area of a circle with a diameter of {diameter} is {circle_area}.")

# Challenge 4: Custom Die Roll

import random

amount_of_die_sides = int(input("Enter how many sides your die will have: "))
roll = random.randint(1, amount_of_die_sides)


