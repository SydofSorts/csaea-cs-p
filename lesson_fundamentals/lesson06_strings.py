# STRING MANIPULATION IN PYTHON
# built-in methods: len(), upper(), lower(), capitalize()

# String formatting, string concatination 

first_name = "Ada"
last_name = "Lovelace"

#Option 1
print("Hello", first_name, last_name, "!")

#Concatenation:
print("Hello" + " " + first_name + " " + last_name + "!")

#f-strings
print(f"Hello, {first_name} {last_name}!")

# 0 1 2 3 4 
# H e l l o
greeting = "Hello"
second_letter = greeting[1]
print(second_letter)

# String indexing and slicing

word = "Super-cali-fragil-istic-expi-ali-docious"

print("\nThe word is:", word)
print("First letter is:", word[0] )
print("Last letter is:", word[-1])
print("Range of letters (non-inclusive)", word[3:7])
print("First five letters:", word[:5])
print("Everything after the first five letters", word[5:] )
print("Last seven letters:", word[-7:])
print("Step through every second charater:", word[::2])
print("String in reverse", word[::-1])

last_name = "     Lovelace"
length = len(last_name) # counts the amount of characters (including spaces) in a string
print("Length of string:", length)

# Challenge 1: Favorite Quote

quote = input("Enter your favorite quote: ")
quote_length = len(quote)
print(f"Your quote is {quote_length} characters long.")


# Challenge 2: 

word = input("Enter a word that is at least 7 character long: ")
print("The second through sixth characters in your word are:", word[1:6])


# Challenge 3: Name Formatter

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Formatted name: {last_name}, {first_name}")




