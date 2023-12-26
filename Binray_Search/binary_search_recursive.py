def binary_search_recursive(arr, target, low, high):
    if low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid  # Element found, return its index
        elif arr[mid] < target:
            return binary_search_recursive(arr, target, mid + 1, high)  # Search the right half
        else:
            return binary_search_recursive(arr, target, low, mid - 1)  # Search the left half
    else:
        return -1  # Element not found

# User input
user_input = input("Enter a sorted list of numbers separated by spaces: ")
sorted_list = [int(num) for num in user_input.split()]

target = int(input("Enter the number to search: "))

# Perform binary search
result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)

if result != -1:
    print(f"The element {target} is present at index {result}.")
else:
    print(f"The element {target} is not present in the list.")