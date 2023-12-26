def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# User input
user_input = input("Enter a non-negative integer to find its factorial: ")

try:
    user_number = int(user_input)
    if user_number >= 0:
        # Calculate the factorial
        result = factorial(user_number)
        print(f"The factorial of {user_number} is: {result}")
    else:
        print("Please enter a non-negative integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")