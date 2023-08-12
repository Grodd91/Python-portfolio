class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.marked = False

class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.num_nodes = 0

    def insert(self, key):
        new_node = FibonacciHeapNode(key)
        if self.min_node is None:
            self.min_node = new_node
        else:
            new_node.right = self.min_node
            new_node.left = self.min_node.left
            self.min_node.left = new_node
            new_node.left.right = new_node
            if key < self.min_node.key:
                self.min_node = new_node
        self.num_nodes += 1

    def extract_min(self):
        min_node = self.min_node
        if min_node:
            if min_node.child:
                child = min_node.child
                while True:
                    next_child = child.right
                    min_node.left.right = child
                    child.right = min_node.right
                    child.left = min_node
                    min_node.right.left = child
                    child.parent = None
                    if next_child == min_node.child:
                        break
                    child = next_child
            min_node.left.right = min_node.right
            min_node.right.left = min_node.left
            if min_node == min_node.right:
                self.min_node = None
            else:
                self.min_node = min_node.right
                self.consolidate()
            self.num_nodes -= 1
        return min_node

    def consolidate(self):
        max_degree = int(self.num_nodes ** 0.5) + 1
        aux = [None] * max_degree

        current = self.min_node
        nodes = [current]
        while current.right != self.min_node:
            current = current.right
            nodes.append(current)

        for node in nodes:
            degree = node.degree
            while aux[degree]:
                other = aux[degree]
                if node.key > other.key:
                    node, other = other, node
                self.link(other, node)
                aux[degree] = None
                degree += 1
            aux[degree] = node

        self.min_node = None
        for node in aux:
            if node:
                if self.min_node is None:
                    self.min_node = node
                else:
                    node.right = self.min_node
                    node.left = self.min_node.left
                    self.min_node.left = node
                    node.left.right = node
                    if node.key < self.min_node.key:
                        self.min_node = node

    def link(self, child, parent):
        child.left.right = child.right
        child.right.left = child.left
        child.parent = parent
