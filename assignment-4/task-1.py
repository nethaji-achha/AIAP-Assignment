# Writing the Python program shows that LEAP YEAR or not.
# def is_leap_year(year):
#     """
#     Return True if year is a leap year, False otherwise.
#     Uses the Gregorian rule:
#       - divisible by 4 -> leap
#       - divisible by 100 -> not leap
#       - divisible by 400 -> leap
#     """
#     if not isinstance(year, int):
#         raise TypeError("year must be an integer")
#     return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

# if __name__ == "__main__":
#     tests = [2000, 1900, 2004, 2001, 2400, 1800]
#     for y in tests:
#         print(f"{y}: {'leap year' if is_leap_year(y) else 'not a leap year'}")

# Writing a Python program shows that the LEAP or not by the input given by the user.

def is_leap_year(year):
    """
    Return True if year is a leap year, False otherwise.
    Uses the Gregorian rule:
      - divisible by 4 -> leap
      - divisible by 100 -> not leap
      - divisible by 400 -> leap
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer")
    return (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))

if __name__ == "__main__":
    import sys

    # If years provided as command-line arguments, check them
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            try:
                y = int(arg)
            except ValueError:
                print(f"Invalid year: {arg}")
                continue
            print(f"{y}: {'leap year' if is_leap_year(y) else 'not a leap year'}")
    else:
        # Prompt the user for a single year, or press Enter to run sample tests
        try:
            s = input("Enter a year (or press Enter to run sample tests): ").strip()
        except EOFError:
            s = ""

        if s == "":
            tests = [2000, 1900, 2004, 2001, 2400, 1800]
            for y in tests:
                print(f"{y}: {'leap year' if is_leap_year(y) else 'not a leap year'}")
        else:
            try:
                year = int(s)
            except ValueError:
                print("Invalid input. Please enter an integer year.")
            else:
                print(f"{year}: {'leap year' if is_leap_year(year) else 'not a leap year'}")
