class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    stack = Stack()
    while True:
        print("\nStack operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Is Empty")
        print("5. Quit")

        choice = input("Enter your choice (1-5): ").strip()
        if choice == "1":
            item = input("Enter item to push: ")
            stack.push(item)
            print(f"Pushed {item} to stack.")
        elif choice == "2":
            try:
                popped = stack.pop()
                print(f"Popped {popped} from stack.")
            except IndexError as e:
                print(e)
        elif choice == "3":
            try:
                top = stack.peek()
                print(f"Top of stack: {top}")
            except IndexError as e:
                print(e)
        elif choice == "4":
            print("Stack is empty." if stack.is_empty() else "Stack is not empty.")
        elif choice == "5":
            print("Quitting.")
            break
        else:
            print("Invalid choice. Please select from 1-5.")

