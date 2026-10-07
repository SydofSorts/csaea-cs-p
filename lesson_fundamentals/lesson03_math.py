#KEY CONCEPTS: math operators: +, -, *, /, //, %, **

add = 4 + 2 + 7
print("Sum:", add)

subtract = 42 - 7
print("Difference:", subtract)

multiply = 4 * 2 * 7
print("Product:", multiply)

float_divide = 42 / 7
print("Float division:", float_divide)

integer_divide = 47 // 2
print("Integer division:", integer_divide)

mod = 24 % 7
print("Modulus: ", mod)

exponent = 7 ** 2
print("Exponent", exponent)

#PEMDAS (Parentheses, Exponents, Multiplication/Division, Addition/Subtraction)

result1 = (2 + 3) * 4
print("Result 1:", result1)

result2 = 2 ** 3 * 4
print("Result 2:", result2)

result3 = 5 + 2 ** 3 * (4 - 1)
print("Result 3:", result3)

# Challenge 1: Rectangle Area  
# Calculate the area of a rectangle with a width of 8 and a height of 5. 
# Create separate variables for width, height, and result. Print result. 

rectangle_width = 8
rectangle_height = 5
rectangle_area = rectangle_width * rectangle_height
print(rectangle_area)

# Challenge 2: Circle Area  
# Use the formula πr² to calculate the area of a circle with radius 7. (Use 3.14 for π.)  
# (Use 3.14 for π.)  
# Separate variables for pi, radius, and result. 

pi = 3.14
circle_radius = 7
circle_area = pi * circle_radius ** 2
print(circle_area)

# Challenge 3: Shopping Total  
# A book costs $12.99 and a notebook costs $3.50.  
# Calculate the total cost for 3 books and 4 notebooks.  
# Use only one print statement. Print the result in this format: 
#     Book: <$ cost of book>
#     Notebook: <$ cost of notebook>
#     Total: <$>

book_cost = 12.99
notebook_cost = 3.50
total_cost = 3 * book_cost + 4 * notebook_cost
print(f"Book: ${book_cost}\nNotebook: ${notebook_cost}\nTotal Cost: ${total_cost}")


# Challenge 4: Even or Odd  
# Use the modulus operator to check if the number 57 is even or odd. 
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd.

number = 57

if number % 2 == 0:
    print("Even")
else:
    print("Odd")





