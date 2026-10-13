# To save for later:
# Doc on libraries: https://docs.python.org/3/library/index.html
# Doc on Math library: https://docs.python.org/3/library/math.html

import math 

sq_root = math.sqrt(25)
print("Square root:", sq_root)

round_up = math.ceil(4.5)
print("Round up: ", round_up)

round_down = math.floor(4.9999)
print(f"Round down: {round_down}")

exponent = math.pow(2,5)
print(exponent)

# CONSTANT - a variable that never changes/will never be updated
# Constant variable names are in ALL CAPS

PI = math.pi
print(PI)

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14. 
# Formulas: the area of a circle is πr² -- the radius is diameter / 2

radius = 7
circle_area = math.pi * math.pow(radius, 2)
print(circle_area)

# PYTHON RANDOM LIBRARY

# Python's library is a Pseudorandom Number Generator (PRNG)

# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.00. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float UP to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10. 

seed = 3.1415
seed1 = math.pow(seed, 2) + 187.45
seed2 = seed1 * 2
seed3 = seed2/5 - 10
result = math.ceil(seed3)
print(f"Random number: {result}")

# MR.HARRELL'S BONUS EXAMPLE

seed = 3535.9
step1 = seed / 6.7
step2 = step1 - 800
step3 = step2 % 10
result = math.ceil(step3)
print("Your random num is:", result)

# Simple version:

seed = 76743

for n in range(5):
    calcs = seed + 2234 * 22 / 3
    randint = math.ceil(calcs)
    print(f"Simple random num gen: {randint % 10}")
    seed += 1


# Pythons random library 

import random

random_integer = random.randint(1,100)
print(random_integer)

random_float = random.random()
print(random_float)

pets = ["cat", "rabbit", "dog", "parrot"]

random_selection = random.choice(pets)
print(random_selection)

random.shuffle(pets)
print(pets)

# Challenge 2: Simulate a Die Roll

die_roll = random.randint(1, 6)
print(f"You landed on {die_roll}!")

# Challenge 3: Random Square Root

num = random.randint(1, 75)
num_sqrt = math.sqrt(num)
num_int = math.ceil(num_sqrt)
print(f"Random Number:{num}\nRandom Number SQRT:{num_sqrt}\nRandom Number SQRT -> Integer:{num_int}")

# Challenge 4: Power Roll

base = random.randint(1, 6)
exponent = random.randint(1, 6)
power_roll = int(math.pow(base, exponent))

print(f"Die 1 (Base):{base}\nDie 2 (Exponent):{exponent}\nResult:{power_roll}")





