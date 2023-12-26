# Perform linear search
result = linear_search_iterative(input_list

def linear_search_recursive(arr, x, index=0):
    if index < len(arr):
        if arr[index] == x:
            return index  # Return the index if the element is found
        else:
            return linear_search_recursive(arr, x, index + 1)  # Recur for the next index
    else:
        return -1  # Return -1 if the element is not in the array

user_input = input("Enter a list of numbers separated by spaces: ")
input_list = [int(num) for num in user_input.split()]

target = int(input("Enter the number to search: "))

result = linear_search_recursive(input_list, target)

if result != -1:
    print(f"The element {target} is present at index {result}.")
else:
    print(f"The element {target} is not present in the list.")