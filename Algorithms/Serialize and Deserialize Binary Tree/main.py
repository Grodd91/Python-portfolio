class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def preorder(node):
        if node:
            result.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        else:
            result.append('#')

    result = []
    preorder(root)
    return ','.join(result)

def deserialize(data):
    def helper():
        val = next(values)
        if val == '#':
            return None
        node = TreeNode(int(val))
        node.left = helper()
        node.right = helper()
        return node

    values = iter(data.split(','))
    return helper()
