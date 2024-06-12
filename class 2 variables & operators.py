# Comment in Python starts with #
# print is a built-in function, it takes arguments/parameters to print on the console
print("Saylani Class 2")

# Variables
# String
# Integer
# Float
# Boolean

# String variables
name = "Hassan"  # String
print(name)
print(type(name))
print(id(name))  # Use print to see the ID

last_name = 'Khan'  # Using single quotations
print(last_name)
print(type(last_name))
print(id(last_name))

# Print a string with escaped quotes
print("Qadi said, \"Today is OFF\"")

# Multi-line string using triple quotes
poem = '''Humpty Dumpty sat on a wall,
Humpty Dumpty had a great fall;
Threescore men and threescore more,
Cannot place Humpty Dumpty as he was before.'''
print(poem)

# Integer variable
age = 15
print(age)
print(type(age))
print(id(age))

# Float variable
weight = 40.545677
print(weight)
print(type(weight))
print(id(weight))

# Boolean variable
is_present = True
print(is_present)
print(type(is_present))
print(id(is_present))

# Operators
print(2 + 2)  # Addition
print(4 - 2)  # Subtraction
print(2 * 2)  # Multiplication
print(6 / 3)  # Division (always returns float)
print(3 ** 2)  # Power
print(5 // 2)  # Floor division

# Ceil division using math module
import math 
x = 5 / 2
y = math.ceil(x)
print("Result is:", y)

# Keywords
# Variables cannot be named using Python keywords

# Using single quotations for strings
var_True = "Qasim"

# Modulus operator returns remainder
print(9 % 4)  

# Compound assignment operators
age += 5  # age = age + 5
print(age)

age -= 5  # age = age - 5
print(age)

age /= 2  # age = age / 2
print(age)

age *= 2  # age = age * 2
print(age)

# Expressions using BODMAS rule
print(1 + 3 - 2 * 4)
print(1 + (3 - 2) * 4)
print(1 + (3 - 2) + 2 ** 4)
print(((2 * 4) * 4) + 2)

# Concatenation
print("Qasim " + "Hassan")
print("Qasim ", "Hassan")  # Will convert it into a tuple
print("Qasim ", "Hassan")  # Will print two strings with a space

# Printing variables
print(name, age, weight, is_present)  # Again it converts into a tuple

# Method 1: Concatenation with , (will do type casting by default)
print("Student Name:", name)
print("Student Age:", age)
print("Student Weight:", weight)
print("Student is Present:", is_present)

# Method 2: Concatenation with + (requires type casting)
print("Student Name: " + name)
print("Student Age: " + str(age))
print("Student Weight: " + str(weight))
print("Student is Present: " + str(is_present))

# Note: This line causes a TypeError because you can't concatenate string and integer directly
# print("The sum of 2 plus 2 is " + 4)

# Corrected version
print("The sum of 2 plus 2 is " + "4")

# Method 3: Concatenation with f-strings (formatting)
print(f"Student Name: {name}")
print(f"Student Age: {age}")
print(f"Student Weight: {weight}")
print(f"Student is Present: {is_present}")

# Creating and printing a full greeting
greeting = "Hello"
separators = ", "
addressee = "World"
punc = "!"
whole_greeting = greeting + separators + addressee + punc
print(whole_greeting)
