def greet_user(name, gender):
    """
    Returns a greeting message with a title based on gender.
    
    Args:
        name (str): The name of the user
        gender (str): The gender (case-insensitive)
            - "male" -> "Mr."
            - "female" -> "Ms."
            - any other -> "Mx."
    
    Returns:
        str: A greeting message formatted as "Hello, [Title] [name]!"
    """
    # Convert gender to lowercase for case-insensitive comparison
    gender_lower = gender.lower().strip()
    
    # Determine the title based on gender
    if gender_lower == "male":
        title = "Mr."
    elif gender_lower == "female":
        title = "Ms."
    else:
        title = "Mx."
    
    # Return the formatted greeting message
    return f"Hello, {title} {name}!"


def main():
    """Main function to get user input and display the greeting."""
    # Ask for user input
    name = input("Please enter your name: ").strip()
    gender = input("Please enter your gender (male/female/other): ").strip()
    
    # Get the greeting message
    greeting = greet_user(name, gender)
    
    # Display the greeting
    print(greeting)


if __name__ == "__main__":
    main()

