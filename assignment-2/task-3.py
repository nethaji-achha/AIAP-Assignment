import math

def calculate_square_area(side):
    """Calculate area of a square."""
    return side * side

def calculate_rectangle_area(length, width):
    """Calculate area of a rectangle."""
    return length * width

def calculate_triangle_area(base, height):
    """Calculate area of a triangle."""
    return 0.5 * base * height

def calculate_circle_area(radius):
    """Calculate area of a circle."""
    return math.pi * radius * radius

def main():
    while True:
        print("\nArea Calculator")
        print("1. Square")
        print("2. Rectangle")
        print("3. Triangle")
        print("4. Circle")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '5':
            print("Goodbye!")
            break
            
        if choice == '1':
            side = float(input("Enter the side length: "))
            area = calculate_square_area(side)
            print(f"Area of square = {area:.2f}")
            
        elif choice == '2':
            length = float(input("Enter the length: "))
            width = float(input("Enter the width: "))
            area = calculate_rectangle_area(length, width)
            print(f"Area of rectangle = {area:.2f}")
            
        elif choice == '3':
            base = float(input("Enter the base: "))
            height = float(input("Enter the height: "))
            area = calculate_triangle_area(base, height)
            print(f"Area of triangle = {area:.2f}")
            
        elif choice == '4':
            radius = float(input("Enter the radius: "))
            area = calculate_circle_area(radius)
            print(f"Area of circle = {area:.2f}")
            
        else:
            print("Invalid choice! Please select 1-5")

if __name__ == "__main__":
    main()

