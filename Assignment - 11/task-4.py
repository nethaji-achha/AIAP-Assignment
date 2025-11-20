class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, root, key):
        if key < root.key:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

if __name__ == "__main__":
    bst = BST()
    while True:
        print("\nBST Operations:")
        print("1. Insert")
        print("2. Inorder Traversal")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ").strip()
        if choice == "1":
            val = input("Enter value to insert: ")
            try:
                key = int(val)
                bst.insert(key)
                print(f"Inserted {key} into BST.")
            except ValueError:
                print("Please enter an integer.")
        elif choice == "2":
            values = bst.inorder_traversal()
            if values:
                print("Inorder Traversal:", " ".join(str(x) for x in values))
            else:
                print("BST is empty.")
        elif choice == "3":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please select from 1-3.")
