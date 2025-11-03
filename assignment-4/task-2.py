def cm_to_inches(cm, precision=None):
    """
    Convert centimeters to inches.
    1 cm = 0.39370078740157477 in

    Args:
        cm (int|float): length in centimeters (must be numeric, non-negative)
        precision (int|None): number of decimal places to round the result to;
                              if None, return full float.

    Returns:
        float: length in inches

    Raises:
        TypeError: if cm is not a number
        ValueError: if cm is negative
    """
    if not isinstance(cm, (int, float)):
        raise TypeError("cm must be a number")
    if cm < 0:
        raise ValueError("cm must be non-negative")

    inches = cm * 0.39370078740157477
    return round(inches, precision) if isinstance(precision, int) else inches

if __name__ == "__main__":
    # Example IO:
    # Input: 10
    # Output: 3.9370 (when precision=4)
    try:
        s = input("Enter length in centimeters: ").strip()
        cm_value = float(s)
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    else:
        print(f"{cm_value} cm = {cm_to_inches(cm_value, precision=4)} in")