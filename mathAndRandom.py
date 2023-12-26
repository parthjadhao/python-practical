import math
import random

# Mathematical operations using the math module
num1 = 10
num2 = 4

# Basic arithmetic operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2

# Exponential and logarithmic operations
power_result = math.pow(num1, num2)
log_result = math.log(num1)

# Trigonometric operations
sin_result = math.sin(math.radians(30))  # Convert degrees to radians for trigonometric functions
cos_result = math.cos(math.radians(60))
tan_result = math.tan(math.radians(45))

# Displaying results of mathematical operations
print("Basic Arithmetic Operations:")
print("Sum:", sum_result)
print("Difference:", difference_result)
print("Product:", product_result)
print("Quotient:", quotient_result)

print("\nExponential and Logarithmic Operations:")
print("Power:", power_result)
print("Natural Logarithm:", log_result)

print("\nTrigonometric Operations:")
print("Sine:", sin_result)
print("Cosine:", cos_result)
print("Tangent:", tan_result)

# Random number operations using the random module
random_integer = random.randint(1, 10)  # Generate a random integer between 1 and 10
random_float = random.uniform(1.0, 10.0)  # Generate a random float between 1.0 and 10.0
random_choice = random.choice(['apple', 'banana', 'cherry'])  # Choose a random element from a list

# Displaying results of random number operations
print("\nRandom Number Operations:")
print("Random Integer:", random_integer)
print("Random Float:", random_float)
print("Random Choice:", random_choice)