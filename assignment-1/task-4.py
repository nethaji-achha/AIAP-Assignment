def find_largest_number(numbers):
    """
    Find the largest number in a list using iteration
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float/int: The largest number in the list
        None: If the list is empty
    """
    if not numbers:  # Check if list is empty
        return None
        
    largest = numbers[0]  # Initialize with first element
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Alternative method using built-in max() function
def find_largest_number_builtin(numbers):
    """
    Find the largest number in a list using built-in max() function
    
    Args:
        numbers (list): List of numbers
        
    Returns:
        float/int: The largest number in the list
        None: If the list is empty
    """
    return max(numbers) if numbers else None

# Example usage
if __name__ == "__main__":
    test_list = [34, 12, 89, 55, 2, 100, 45]
    print(f"Test list: {test_list}")
    print(f"Largest number (iteration): {find_largest_number(test_list)}")
    print(f"Largest number (built-in): {find_largest_number_builtin(test_list)}")