class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def max_depth(root):
    if not root:
        return 0

    max_child_depth = 0
    for child in root.children:
        max_child_depth = max(max_child_depth, max_depth(child))

    return max_child_depth + 1
