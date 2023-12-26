import sys

# Get the total number of command line arguments
num_arguments = len(sys.argv) - 1  # Subtracting 1 to exclude the script name itself

# Print the number of arguments
print(f"Number of command line arguments: {num_arguments}")

# Print the actual arguments
if num_arguments > 0:
    print("Arguments:")
    for i in range(1, num_arguments + 1):
        print(f"Argument {i}: {sys.argv[i]}")