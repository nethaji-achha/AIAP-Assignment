# Program to take inputs A and B and print A+B

# Take input from user for A
A = input("Enter value for A: ")

# Take input from user for B
B = input("Enter value for B: ")

# Convert inputs to float to handle both integers and decimals
# If you want only integers, use int() instead
try:
    A = float(A)
    B = float(B)
    result = A + B
    print(f"A+B = {result}")
except ValueError:
    # If inputs are not numbers, treat as strings and concatenate
    print(f"A+B = {A + B}")

