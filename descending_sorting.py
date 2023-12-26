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

# Perform descending sorting
sorted_numbers_desc = sorted(numbers, reverse=True)

# Display the sorted list in descending order
print("Sorted numbers in descending order:", sorted_numbers_desc)