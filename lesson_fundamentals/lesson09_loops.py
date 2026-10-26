# LOOPS/ITERATIONS IN PYTHON
# Loops repeat a block of code until they hit a limit or condition.
# They exist to save us from typing the same line 500 times.
# Python gives us for-loops and while-loops.

import time 

# The FOR-LOOP.
# A for-loop repeats for each element in a sequence (like a list or string).

animals = ["rabbit", "fish", "parrot", "dog", "cat"]
print("My animals:", animals)

#for animal in animals:
    #print("I shall now pet a", animal)
    #time.sleep(1) # pause for half a second

# We can loop a specific number of times using range(start[inclusive], stop[exclusive], step).
# Common to use "i" as placeholder variable, meaning index

# for i in range(5):
#     print("Counting", i)

# for num in range(1, 11, 3):
#     print("Numbers be like:", num)

# fav_word = "Kipsulheris"
# print(fav_word)
# letter_list = []

# for letter in fav_word:
#     print(letter)
#     letter_list.append(letter + "!")
#     time.sleep(0.427)

# print(letter_list)

# Challenge 1: Sum Calculator

sum = 0
for num in range(1, 11):
    sum += num

print("Sum:",sum)


# A while-loop repeats *while* a condition is true.
# If you forget to change the condition, it loops forever.
# And then your program becomes immortal. Avoid that.

# += to add to a variable, -= to subtract to a variable, = to overright 

# count = 0 

# while count < 5:
#     print(f"Loopin' -- We are on loop index # {count}")
#     count += 1
#     time.sleep(0.5)

# Example with user input 

# user_input = ""

# while user_input != "exit":
#         user_input = input("Type 'exit' to leave this place: ")

# Loop Control Statements

for i in range (1,11):

     if i == 3:
          print("Skipping 3") # skips this iteration
          continue
     if i == 6:
          print("Breaking at 6")
          break # stop the loop entirely
     if i == 9:
        pass # place holder. does nothing. will code in the future

     print("Number", i)


# Challenge 2: Guess Until Correct

user_num = ""

while user_num != "7":
    user_num = input("Give me a number: ")