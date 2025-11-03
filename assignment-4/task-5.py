def count_lines_in_txt(filepath="Source.txt"):
    """
    Return the number of lines in a .txt file (default: "Source.txt").

    Examples (few-shot):
      - File content:
          Hello world
          This is a test file
        -> returns 2

      - File content:
          Line one
          Line two
          Line three
        -> returns 3
    """
    import os

    if not isinstance(filepath, str):
        raise TypeError("filepath must be a string")
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No such file: {filepath}")

    with open(filepath, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)

if __name__ == "__main__":
    # Read default "Source.txt" or prompt for a path
    path = input("Enter path to .txt file (press Enter for 'Source.txt'): ").strip() or "Source.txt"
    try:
        lines = count_lines_in_txt(path)
    except Exception as e:
        print(f"Error: {e}")
    else:
        print(f"Number of lines: {lines}")