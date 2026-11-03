import random
import math
import time 

# I can comment for clarity

print("\tI know how \nto print")

variable = "store_ data"

string = "Hi"
integer = 14
boolean = True 
float = 4.27

# Float's can represent fractional values as they have a decimal place

math = 6*3/2+5-8 # P E M D A S 
print(math)

print("Hi"+" "+variable+" "+"you")
print(f"Hi {variable.upper()} you")

print(len(variable)) # 11 characters in the string (INCLUDES SPACES)

store = int(input("Enter your age: "))
three_yrs_ltr = store + 3
print(f"Your age in three years is {three_yrs_ltr}")

rand_float = random.random()
print(rand_float)

# > (greater than); < (less than); >= (greater than or equal to); <= (less than or equal to); 
# == (comparing to see if things are equal) != (comparing to see if things are not equal)
# % (remainder ex. 4 % 2 --> 0)

if three_yrs_ltr >= 18:
    print("Welcome in!")
elif three_yrs_ltr < 18 and three_yrs_ltr >= 11:
    print("Get a guardian.")
else:
    print("Your better than this, kid.")


expl_list = ["string", 427, 3.14159, True]
expl_list.append(8.99)
print(expl_list)



