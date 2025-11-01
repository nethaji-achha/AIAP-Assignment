def is_prime(n):
    # Numbers less than 2 are not prime
    if n < 2:
        return False
    
    # Check for divisibility from 2 to sqrt(n)
    for i in range(2, int(n ** 0.5) ):
        if n % i == 0:
            return False
    return True

# Get input from user
number = int(input("Enter a number to check if it's prime: "))

# Check and display result
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")
