def is_palindrome(string):
    # Convert to lowercase and keep only alphanumeric characters
    cleaned_str = ''.join(char.lower() for char in string if char.isalnum())
    
    # Compare the string with its reverse
    return cleaned_str == cleaned_str[::-1]

def is_palindrome_two_pointer(string):
    """
    Check if a string is a palindrome using two-pointer technique
    
    Args:
        string (str): Input string to check
        
    Returns:
        bool: True if string is palindrome, False otherwise
    """
    # Convert to lowercase and keep only alphanumeric characters
    cleaned_str = ''.join(char.lower() for char in string if char.isalnum())
    
    # Initialize two pointers
    left = 0
    right = len(cleaned_str) - 1
    
    # Compare characters from both ends moving towards center
    while left < right:
        if cleaned_str[left] != cleaned_str[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test cases
if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "hello",
        "12321"
    ]
    
    for test in test_cases:
        result1 = is_palindrome(test)
        result2 = is_palindrome_two_pointer(test)
        print(f"'{test}':")
        print(f"Method 1: {'' if result1 else 'not '}a palindrome")
        print(f"Method 2: {'' if result2 else 'not '}a palindrome")
        print()