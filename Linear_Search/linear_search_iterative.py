def linear_search_iterative(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

user_input = input("Enter a list of numbers separated by spaces: ")
input_list = [int(num) for num in user_input.split()]

target = int(input("Enter the number to search: "))

result = linear_search_iterative(input_list, target)

if result != -1:
    print(f"The element {target} is present at index {result}.")
else:
    print(f"The element {target} is not present in the list.")