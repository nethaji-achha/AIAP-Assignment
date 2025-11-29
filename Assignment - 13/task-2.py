def read_file():
    filename = input("Enter the filename: ")

    try:
        with open(filename, "r") as f:
            data = f.read()
        return data
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."
    except PermissionError:
        return f"Error: Permission denied when accessing '{filename}'."
    except Exception as e:
        return f"An unexpected error occurred: {e}"

with open("sample.txt", "w") as f:
    f.write("This is a sample file for testing.\nIt has two lines.")

# Run the function
print(read_file())
