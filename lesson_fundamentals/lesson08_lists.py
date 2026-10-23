# LISTS IN PYTHON
# Lists store multiple values in one variable.
# They are ordered, mutable (changeable), and allow duplicates.

empty_list = []

# CREATE LISTS 

animals = ["llama", "bunny", "penguin"]
numbers = [0, 4, 2, 7, 1]
mixed = ["kipsulheris", 427, True, 6.77]

print("Animals list:", animals)
print("Numbers list:", numbers)
print("Mixed data types list", mixed)

# print the third element in animals.
print(animals[2])

# print the last element in numbers
print(numbers[-1])

#print the first element in the mixed list
print(mixed[0])

# change an element of a list

animals[-1] = "pink fairy armadillo"
print(animals)

# add elements to the end of a list

animals.append("glass frog")
print(animals)

# insert element at specific index 
animals.insert(2, "chickadee")
print(animals)
animals.insert(1, "alpaca")

# remove elements

animals.remove("llama")
print(animals)

# remove (pop off) last element and save it into a variable

last_animal = animals.pop()
print(last_animal)
print(animals)

### **Challenge 1: Number Swap**

counting_numbers = [1, 2, 3, 4, 5, 6]
user_int = input("Enter an integer: ")
counting_numbers[2] = int(user_int)
print(counting_numbers)

### **Challenge 2: Shopping List Manager**

# Initialize an empty list called `shopping`.

shopping = []

shopping.append("meat")
shopping.append("cheese")
shopping.append("crackers")
shopping.insert(1, "grapes")
shopping.remove("meat")
print(shopping)

nums = [3, 7, 1, 9, 4, 2, 5, 8, 6, 0]
print("Numbers:", nums)

print("Length of list:", len(nums))
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum", sum(nums))

nums.sort()
print(nums)

animals.sort()
print(animals)

nums.reverse()
print(nums)

if "dog" in animals:
    print("Dog is in the list")
else:
    print("Dog is not in the list :(")

### Challenge 3: Number Stats

measurements = [4.27, 8.7777, 1.1, 35.7, 0.3636]
print("Length of list:", len(measurements))
print("Minimum:", min(measurements))
print("Maximum:", max(measurements))
print("Sum", sum(measurements))
