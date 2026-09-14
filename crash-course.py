import math

# comment
# Trick: highlight all text you want as comments, use ctrl + / to turn all text to comments

print("Hello World!")

# VARIABLE DECLARATIONS & DATA TYPES: 

a = 4        # integer (Whole Number)
b = 5.5      # float   (Decimal)
c = "CSAEA"  # string  ("letter[s]")
d = True     # boolean (True or False)

print(a, b, c, d)

# MATH OPERATORS

# + (addition and concatenation)
# - (subtraction)
# * (multiplication)
# / (division)

# %  (modulus a.k.a remainder)
# ** (to the power of)
# // (division rounded to the nearest whole number)

# =  (assigning/setting a data type to a variable)
# += (add value to variable and updates/reassigns its value)
# -= (subtract value from variable and updates/reassigns its value)
# /= (divides value from variable and updates/reassigns its value)

e = 3 - 1
e /= 2

# F(ORMATED)-STRING 

print(f"e is equal to {e}")

e -= 7 
e += 12

print(f"e is NOW equal to {e}")

# COMPARISONS (booleans, which always return True of False)

# <  (less than)
# >  (greater than) 
# <= (less than or equal to)
# >= (greater than or equal to) 
# == (comparing if two values are equal | "is equal to")
# != (not equal)

print(4 <=  5)
print(7 == 4)
print(1 != 2)

isEqual = "Yes" != "YES"
print(isEqual)

# LOGICAL OPERATORS
# In order of precedence: 1. not (opposite boolean/"flip it")     2. and     3. or

t = True  # Cancels out False when using or
f = False # Cancels out True when using and

print(not f) #True
print(f and t) #False
print(f or t) #True
print(f or t and not f) #True

# CASTING (transforming one data type to another)

# int (transforming to integer) *IMPORTANT*
# str (transforming to string)

g = int(5.934567898765)
print(g)

# STRINGS

s1 = "Goodnight"
s2 = " and "
s3 = "Goodbye"
end = s1 + s2+ s3 # concatenation with +
end += ", Cowboy."

print(end + "\n") # \n == new line (escaped character)

# MATH LIBRARY

print(math.sqrt(16)) # square root
print(math.ceil(3.65)) # ceiling (round up)
print(math.floor(8.94)) # floor (round down)
print(math.pow(2, 4)) # "to the POWer of" 
# . = "run this function (sqrt) in this library (math)"

#CONDITIONALS

#if    else   elif

t = True
f = False 

if f: 
    print("Reached the first condition")
elif t:
    print("Reached second condition")
else: 
    print("Reached else")

# stops running code when one of the conditions become true (top to bottom) | if none are true it resorts to "else"

if 1 > 1 and 1 == 1:  # False
    print("Reached the first condition")
elif 6 == 7 or 2 != 3: # True
    print("Reached second condition") # --> Stop code here since conditions have been met and print
elif 9 != 0:
    print("Reached third condition")
else: 
    print("Reached else")

# LISTS
# A list can hold any type, and can grow or shrink at any time

nums = [427, 5, 12, 16, 0]
#index   0   1   2   3  4  (ALWAYS start at 0)

print(nums[2]) # print(list[index])
print(nums[0])
print(nums[-3]) # wraps back around/goes backwards in list
print(nums[0] + nums[2])

nums[0] = "Stanley"
print(nums)

# LIST METHODS
# Special built-in methods

words = []
#list.method(argument)
words.append("My") # append = "add something to the end"
words.append("name")
words.append("is")
words.append("Nobody")
print(words)
words.remove("Nobody")
words.insert(3, "Odysseus")
print(words)
words[3] = "Ozymandias"
print(words)
length = len(words)
print(length)

# ITERATION

# For Loop
# A for loop will iterate over a RANGE
# A range is a range of numbers
# range(stop), range(start, stop), range (start, stop, step) | Step = "counting by"

# i = individual element(s)/index
for i in range(5):
    print(i)

# list variable = [element, element, element]
animals = ["sheep", "deer", "moose"]

for animal in animals:
    print(f"We saw {animal}")

nums = [5.1, 3.4, 4.6, 6.8, 9.3, 1.2]

# for number in nums:
#     print(number + 1)

for i in range(len(nums)):
    print(nums[i])

# Debugging 

# print(len(nums))
# print(range(5))

# for i in range(inclusive, exclusive) | inclusive (include this index); exclusive (exclude this index)
# for i in range(0,5):
#     print(nums[i])

# While Loop
# iterates while a condition is true
# when the condition becomes false, it stops

x = 5

while x < 10:
    print(x)
    x += 1

t = True
f = False

while t or f:
    print("hi")