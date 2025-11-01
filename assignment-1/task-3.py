# Program to find the factorial of a number
def factorial(n):
    # If the number is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # For all other numbers, multiply n by factorial of (n-1)
    else:
        return n * factorial(n-1)

# Take input from user
try:
    num = int(input("Enter a positive integer: "))
    
    # Check if the number is negative
    if num < 0:
        print("Factorial cannot be calculated for negative numbers")
    else:
        result = factorial(num)
        print(f"The factorial of {num} is {result}")
except ValueError:
    print("Please enter a valid integer")