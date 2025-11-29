# Here is the redundant code to be refactored:

def calculate_area(shape, x, y=0):
    if shape == "rectangle":
        return x * y
    elif shape == "square":
        return x * x
    elif shape == "circle":
        return 3.14 * x * x
shape = input("Enter the shape (rectangle/square/circle): ").strip().lower()
if shape == "rectangle":
    x = float(input("Enter the length: "))
    y = float(input("Enter the width: "))
    area = calculate_area(shape, x, y)
elif shape == "square":
    x = float(input("Enter the side length: "))
    area = calculate_area(shape, x)
elif shape == "circle":
    x = float(input("Enter the radius: "))
    area = calculate_area(shape, x)
else:
    print("Invalid shape.")
    area = None

if area is not None:
    print(f"The area of the {shape} is: {area}")

# Please refactor the above function to remove redundancy in the code.
