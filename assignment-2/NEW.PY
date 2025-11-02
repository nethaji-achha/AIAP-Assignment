import re
import sys

def is_palindrome(value: object, *, ignore_non_alnum: bool = True, case_insensitive: bool = True) -> bool:
    """Return True if value is a palindrome.
    Accepts str/int/float; converts to string. By default ignores non-alphanumeric chars and is case-insensitive.
    """
    s = str(value)
    if case_insensitive:
        s = s.lower()
    if ignore_non_alnum:
        s = re.sub(r'[^a-z0-9]', '', s)
    return s == s[::-1]

if __name__ == "__main__":
    # Accept input from command line or prompt the user
    if len(sys.argv) > 1:
        text = ' '.join(sys.argv[1:])
    else:
        text = input("Enter text to check palindrome: ")
    print("Palindrome" if is_palindrome(text) else "Not palindrome")