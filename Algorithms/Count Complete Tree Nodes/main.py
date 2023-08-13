class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def count_nodes(root):
    if not root:
        return 0

    left_height = get_left_height(root)
    right_height = get_right_height(root)

    if left_height == right_height:
        return 2 ** left_height - 1
    else:
        return count_nodes(root.left) + count_nodes(root.right) + 1

def get_left_height(node):
    height = 0
    while node:
        height += 1
        node = node.left
    return height

def get_right_height(node):
    height = 0
    while node:
        height += 1
        node = node.right
    return height
