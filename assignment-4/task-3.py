def format_name(full_name):
    """
    Format a full name as "Last, First".
    - The last whitespace-separated token is treated as the last name.
    - Any preceding tokens are treated as the first name (keeps middle names).
    - A single token is returned unchanged.
    """
    if not isinstance(full_name, str):
        raise TypeError("full_name must be a string")
    name = full_name.strip()
    if not name:
        return ""
    parts = [p for p in name.split() if p]
    if len(parts) == 1:
        return parts[0]
    last = parts[-1]
    first = " ".join(parts[:-1])
    return f"{last} {first}"

if __name__ == "__main__":
    # Take input from the user first
    user_input = input("Enter full name: ").strip()
    if user_input:
        print(format_name(user_input))
    else:
        print("No name entered.")

    # Few-shot examples
    examples = [
        ("John Doe", "Doe, John"),
        ("Ada Lovelace", "Lovelace, Ada"),
        ("Mary Ann Smith", "Smith, Mary Ann"),
    ]
    print("\nExamples:")
    for inp, out in examples:
        print(f'Input: "{inp}" -> Output: "{format_name(inp)}"')