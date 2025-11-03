#Prompt : Write a Python function that counts the number of vowels (a, e, i, o, u) in a given string.
def count_vowels(string, case_sensitive=False):
    """
    Count the number of vowels in a string.
    
    Args:
        string (str): Input string to check for vowels
        case_sensitive (bool): If True, treats 'a' and 'A' as different
    
    Returns:
        int: Number of vowels in the string
        
    Example:
        >>> count_vowels("Hello World")
        3
        >>> count_vowels("HELLO WORLD", case_sensitive=True)
        2
    """
    if not isinstance(string, str):
        raise TypeError("Input must be a string")
        
    vowels = 'aeiou'
    if case_sensitive:
        return sum(1 for char in string if char in vowels or char in vowels.upper())
    return sum(1 for char in string.lower() if char in vowels)

if __name__ == "__main__":
    # Test with user input
    test_string = input("Enter a string to count vowels: ")
    result = count_vowels(test_string)
    print(f"Number of vowels: {result}")
    
    # Example test cases
    test_cases = [
        "Hello World",    # 3 vowels
        "Python",         # 1 vowel
        "AEIOU",         # 5 vowels
        "rhythm"         # 0 vowels
    ]
    
    print("\nTest cases:")
    for test in test_cases:
        print(f'"{test}": {count_vowels(test)} vowels')
