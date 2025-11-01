# Function to reverse a string
def reverse_string(s):
    return s[::-1]

# Get input from user
user_input = input("Enter a string to reverse: ")

# Reverse the string and display the result
reversed_string = reverse_string(user_input)
print(f"The reversed string is: {reversed_string}")