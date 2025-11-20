class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(elements) if elements else "List is empty.")

if __name__ == "__main__":
    sll = SinglyLinkedList()
    while True:
        print("\nSingly Linked List Operations:")
        print("1. Insert at End")
        print("2. Insert at Beginning")
        print("3. Display List")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            val = input("Enter value to insert at end: ")
            sll.insert_at_end(val)
        elif choice == "2":
            val = input("Enter value to insert at beginning: ")
            sll.insert_at_beginning(val)
        elif choice == "3":
            sll.display()
        elif choice == "4":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select from 1-4.")
