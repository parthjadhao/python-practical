def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    # Check for factors from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Found a factor, so the number is not prime

    return True  # No factors found, so the number is prime

# User input
user_input = input("Enter a positive integer to check if it's prime: ")

try:
    user_number = int(user_input)
    if user_number >= 0:
        # Check if the entered number is prime
        if is_prime(user_number):
            print(f"{user_number} is a prime number.")
        else:
            print(f"{user_number} is not a prime number.")
    else:
        print("Please enter a non-negative integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")