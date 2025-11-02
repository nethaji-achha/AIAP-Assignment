def calculate_sums(numbers):
    """Calculate the sum of even and odd numbers in a list."""
    even_sum = sum(num for num in numbers if num % 2 == 0)
    odd_sum = sum(num for num in numbers if num % 2 != 0)
    return even_sum, odd_sum

def get_user_input():
    """Get numbers from user input and return as a list."""
    try:
        input_string = input("Enter numbers separated by spaces: ")
        return [int(num) for num in input_string.split()]
    except ValueError:
        print("Invalid input! Please enter valid integers separated by spaces.")
        return []

def main():
    # Get numbers from user
    numbers = get_user_input()
    
    if numbers:
        # Calculate sums
        even_sum, odd_sum = calculate_sums(numbers)
        
        # Print results
        print(f"\nList of numbers: {numbers}")
        print(f"Sum of even numbers: {even_sum}")
        print(f"Sum of odd numbers: {odd_sum}")

if __name__ == "__main__":
    main()