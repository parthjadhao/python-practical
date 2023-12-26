# User input for 5 numbers
numbers = []
for i in range(5):
    user_input = input(f"Enter number {i+1}: ")
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()

# Perform ascending sorting
sorted_numbers = sorted(numbers)

# Display the sorted list
print("Sorted numbers in ascending order:", sorted_numbers)