class Student:
    """
    Represents a student with a name, age, and a list of marks in three subjects.
    """

    def __init__(self, name, age, marks):
        """
        Initializes a new Student object.

        Args:
            name (str): The student's name.
            age (int): The student's age.
            marks (list of int or float): The student's marks in three subjects.
        """
        self.name = name
        self.age = age
        if isinstance(marks, list) and len(marks) == 3:
            self.marks = marks
        else:
            raise ValueError("Marks should be a list of three numeric values")

    def details(self):
        """
        Prints the student's details in a readable format.
        """
        print(f"Name: {self.name}\nAge: {self.age}")

    def total_marks(self):
        """
        Returns the total of the student's marks.

        Returns:
            int or float: The sum of the three marks.
        """
        return sum(self.marks)

# Example usage
if __name__ == "__main__":
    # Sample input values
    student = Student(name="Alice", age=20, marks=[85, 90, 78])
    student.details()
    print(f"Marks: {student.marks}")
    print(f"Total Marks: {student.total_marks()}")
