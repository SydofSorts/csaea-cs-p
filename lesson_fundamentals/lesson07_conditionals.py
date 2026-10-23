# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

# Boolean refresher:
# always return either True or False

print(3==2)
print("Hello" == "Hi there")
print(7 != 4) # ! = bang opperator 
print(4 > 5)

# if 
num = 10 # only runs if condition is true
if num == 10:
    print("Your num is equal to 10")

# if else
num = 5
if num <= 12:
    print("Your num is less than or equal to 12")
else:
    print("Your num is greater than 12")

# if elif else
temp = 52
if temp > 95:
    print("It's HOT!")
elif temp >= 60:
    print("It's nice :)")
else:
    print("It's cold...")

print()

x = 2
y = 20

if x == y:
    print("x is equal to y")
elif x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("ERROR")

# Logical operators: and 
# Both sides of the 'and' must  be true, otherwise it's false. 
age = 16
has_permission = True

if age >= 16 and has_permission == True:
    print("You can drive!")
else:
    print("You can't drive yet.")

# Logical operators: 'or' and 'not'

day = "Sunday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend! :D")
else:
    print("It's the weekday...;(")

# Using 'is' and 'not' 

if day is not "Monday":
    print("It's not Monday! YAY!")


# Challenge 1: Movie Admission

user_age = input("Enter your age: ")
age = int(user_age)

if age < 13:
    print("You can watch PG or G movies.")
elif age >= 13 and age <= 17:
    print("You can watch PG-13 movies.")
elif age >= 18:
    print("You can watch any movie.")


# Challenge 2: Leap Year

user_year = input("Enter a year: ")
year = int(user_year)

if year % 4 != 0:
    print("It is not a leap year.")
elif year % 100 != 0 and year % 4 == 0:
    print("It is a leap year!")
elif year % 100 == 0 and year % 4 == 0 and year  % 400 == 0:
    print("It is a leap year!")
elif year % 100 == 0 and year % 4 == 0 and year  % 400 != 0:
    print("It is not a leap year.")




