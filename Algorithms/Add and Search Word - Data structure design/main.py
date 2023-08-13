class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        def search_in_node(word, node):
            for i, char in enumerate(word):
                if char not in node.children:
                    if char == '.':
                        for child in node.children:
                            if search_in_node(word[i + 1:], node.children[child]):
                                return True
                    return False
                else:
                    node = node.children[char]
            return node.is_end_of_word

        return search_in_node(word, self.root)
