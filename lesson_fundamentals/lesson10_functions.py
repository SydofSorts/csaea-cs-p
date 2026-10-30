# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp# Python functions are simply blocks of code that can be reused. 
# To run a function, you *call* the function by writing its name, followed by parenthesis, and any arguments that it needs.

# https://www.w3schools.com/python/python_functions.asp

def say_hi():
    print("Hi :D")

def say_bye():
    print("Bye :(")

say_hi()
say_bye()
say_bye()
say_hi()
say_bye()

# Functions more commonly RETURN values, not merely print
# We can pass an ARGUMENT into a function's PARAMETER

def express_this(e): # e is called a PARAMETER, which is a placeholder for an ARGUMENT
    return e

expression = express_this("Kipsulheris") # the mathmatical expression here is the ARGUMENT, the actual value that will be used by a functions PARAMETER
print(expression)

def greeter(name):
    return f"Hi {name}"

first = greeter("Thomas Aldin")
second = greeter("Raymond Beckett")
third = greeter("Cooper Hant") 

print(first, second, third)

def remainder(a,b):
    return a % b

result = remainder(42,7)
print(result)

def is_far(distance):
  if distance >= 100:
        return "That's far"
  if distance < 100 and distance > 20:
        return "Ehhhh...That's not too far"
  if distance <= 20:
        return "Hey that's pretty close by!"

distance1 = is_far(427)
distance2 = is_far(27)
distance3 = is_far(7)
distance4 = is_far(20)
print(f"{distance1}\n{distance2}\n{distance3}\n{distance4}")


# Doubler Challenge

def doubler(num,times):
    num_list = []
    for i in range(times):
        num = num * 2
        num_list.append(num)

    print(num_list)  # (Added while watching Mr. Harrell's example)
    return num_list # (Added while watching Mr.Harrell's example)

doubler(1, 5)


# Challenge 1: Calculator

def adder(a, b):
    return a + b

sum = adder(1,7)
print(sum)

def subtracter(a, b):
    return a - b

difference = subtracter(5, 6)
print(difference)

def divider(a, b):
    return a/b

quotient = divider(27, 3)
print(quotient)

def multiplier(a, b):
    return a*b

product = multiplier(5, 3)
print(product)

# Challenge 2: Average

def average (a, b, c, d, e):
    return (a+b+c+d+e)/5

avrg_inpt = average(1, 2, 3, 4, 7)
print(avrg_inpt)

# Challenge 3: Even or Odd

def is_even(a):
    if a % 2 == 0:
        return print("Even")
    else:
        return print("Odd")

num = is_even(9)


# Challenge 4
# Use the pseudocode below to write code:
# Make a function called "analyze_word" that counts how many vowels and consonants are in a word
# Tools: uses a for loop, IF/THEN statement, "aeiou".

# The function analyze_word accepts one argument, a single word (string):
# Initialize two variables:
# vowelCount set to 0
# consonantCount set to 0
# Use a loop to iterate through each character in the word.
# Inside the loop, use an IF/ELSE statement:
# If the character is a vowel (a, e, i, o, u), increment vowelCount.
# Otherwise, increment consonantCount.
# After the loop ends: 
# 	return a string that states how many vowels and how many consonants are in the word.

# Call the function with a sample one-word string and print the returned result outside the function

def analyze_word(word):
    vowelCount = 0
    consonantCount = 0
    for letter in word:
        if letter == ["a", "e", "i", "o", "u"]:
            vowelCount += 1
            return print(f"Your word has {vowelCount} vowels")

word = analyze_word("cat")
print(word)


