class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    elif value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def search(root, value):
    if root is None or root.value == value:
        return root
    if value < root.value:
        return search(root.left, value)
    return search(root.right, value)

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.value)
        inorder_traversal(root.right)

# Usage example

# Creating the tree
root = None
root = insert(root, 3   57)
root = insert(root, 134)
root = insert(root, 673)
root = insert(root, 722)
root = insert(root, 544)
root = insert(root, 368)
root = insert(root, 568)

# Searching the tree
found_node = search(root, 4)
if found_node:
    print("Found node with value:", found_node.value)
else:
    print("Node with the given value not found")

# Inorder traversal of the tree
print("Inorder traversal of the tree:")
inorder_traversal(root)
