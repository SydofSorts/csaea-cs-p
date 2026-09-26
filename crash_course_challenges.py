import math

# CHALLENGE 1: TIP CALCULATOR

bill = 50
tip = bill * 0.2
total = tip + bill 

print(f"Tip:{tip}\nTotal:{total}" )

# CHALLENGE 11: ROCKET LAUNCH 

start = 10

for integer in range(start, 0, -1):
   print(integer)

if integer == 1:
   print("Liftoff!")

# CHALLENG #4: REPORT CARD

score = 70

if score >= 90:
   print("A")
elif score < 90 and score >= 80:
   print("B")
elif score < 80 and score >= 70:
   print("C")
elif score < 70 and score >= 60:
   print("D")
else:
   print("F")

# CHALLENGE #2: PIZZA ORDER

students = 23
slices_per_student = 2
slices_per_pizza = 8

exact_number_of_pizzas = (students*slices_per_student)/slices_per_pizza
whole_pizzas = math.ceil(exact_number_of_pizzas)
extra_slices = int(whole_pizzas*8 - exact_number_of_pizzas*8)

print(f"Order {whole_pizzas} pizzas\nExtra Slices: {extra_slices}")

# CHALLENGE #3: TEMPERATURE CONVERTER

fahrenheit = 212
celsius_conversion = (fahrenheit - 32) * 5 / 9

print(f"{fahrenheit} F is {celsius_conversion} C")

# CHALLENGE #20: SPEED TRAP

speed_limit = 55
speed = 71

if speed <= speed_limit:
   print("Good job, keep up the safe driving")
elif speed >= speed_limit + 1 and speed <= speed_limit + 10:
   print("Warning: Slow down and drive safe")
elif speed >= speed_limit + 10 and speed <= speed_limit + 20:
   print("Fine: $100")
else:
   print("Fine: $250")











