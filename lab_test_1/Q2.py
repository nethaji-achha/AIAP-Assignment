class Rectangle:
    """
    Manual docstring:
    A class to represent a rectangle.
    Provides methods to calculate the area and perimeter of the rectangle.
    """

    def __init__(self, width, height):
        """
        Manual docstring:
        Initializes a Rectangle instance with given width and height.

        AI-generated:
        Initialize the Rectangle object with width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Manual docstring:
        Calculates and returns the area of the rectangle.

        AI-generated:
        Calculate the area of the rectangle.

        Returns:
            float: The area (width * height) of the rectangle.
        """
        # Manual comment: Multiply width by height to get area
        return self.width * self.height

    def perimeter(self):
        """
        Manual docstring:
        Calculates and returns the perimeter of the rectangle.

        AI-generated:
        Calculate the perimeter of the rectangle.

        Returns:
            float: The perimeter (2 * (width + height)) of the rectangle.
        """
        # Manual comment: Add width and height, then multiply by 2 for perimeter
        return 2 * (self.width + self.height)


# Comparison of manual vs AI-generated documentation:
# The AI-generated docstrings are concise, focus on functionality, and often use phrases like "Calculate the ...".
# Manual docstrings allow inclusion of clarifying information or intent, but may be more verbose.
# Inline comments also differ: AI tends to make brief, objective remarks, while manual comments may provide more reasoning.

# Example usage
if __name__ == "__main__":
    try:
        length = float(input("Enter the length of the rectangle: "))
        breadth = float(input("Enter the breadth of the rectangle: "))
        rect = Rectangle(length, breadth)
        print("Area:", rect.area())
        print("Perimeter:", rect.perimeter())
    except ValueError:
        print("Invalid input. Please enter numerical values for length and breadth.")


