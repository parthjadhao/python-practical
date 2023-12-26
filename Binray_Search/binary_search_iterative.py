def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            low = mid + 1  # Search the right half
        else:
            high = mid - 1  # Search the left half

    return -1  # Element not found

# User input
user_input = input("Enter a sorted list of numbers separated by spaces: ")
sorted_list = [int(num) for num in user_input.split()]

target = int(input("Enter the number to search: "))

# Perform binary search
result = binary_search_iterative(sorted_list, target)

if result != -1:
    print(f"The element {target} is present at index {result}.")
else:
    print(f"The element {target} is not present in the list.")