class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

if __name__ == "__main__":
    queue = Queue()
    while True:
        print("\nQueue operations:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Is Empty")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            item = input("Enter item to enqueue: ")
            queue.enqueue(item)
            print(f"Enqueued {item} to queue.")
        elif choice == "2":
            try:
                dequeued = queue.dequeue()
                print(f"Dequeued {dequeued} from queue.")
            except IndexError as e:
                print(e)
        elif choice == "3":
            print("Queue is empty." if queue.is_empty() else "Queue is not empty.")
        elif choice == "4":
            print("Quitting.")
            break
        else:
            print("Invalid choice. Please select from 1-4.")

