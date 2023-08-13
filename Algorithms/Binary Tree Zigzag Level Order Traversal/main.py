class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzag_level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])
    level = 0

    while queue:
        level_nodes = []
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            if level % 2 == 0:
                level_nodes.append(node.val)
            else:
                level_nodes.insert(0, node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_nodes)
        level += 1

    return result
