def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit)**num_digits for digit in num_str)
    
    return armstrong_sum == number

# User input
user_input = input("Enter a positive integer to check if it's an Armstrong number: ")

try:
    user_number = int(user_input)
    if user_number >= 0:
        # Check if the entered number is an Armstrong number
        if is_armstrong(user_number):
            print(f"{user_number} is an Armstrong number.")
        else:
            print(f"{user_number} is not an Armstrong number.")
    else:
        print("Please enter a non-negative integer.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")