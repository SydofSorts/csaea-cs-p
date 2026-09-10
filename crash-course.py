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
# += (add value to variable and updates its value)
# -= (subtract value from variable and updates its value)
# /= (divides value from variable and updates its value)

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

f = False # Cancels out True when using and
t = True  # Cancels out False when using or

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