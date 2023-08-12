import mmh3

class BloomFilter:
    def __init__(self, size, num_hash_functions):
        self.size = size
        self.num_hash_functions = num_hash_functions
        self.bit_array = [False] * size

    def add(self, element):
        for i in range(self.num_hash_functions):
            hash_value = mmh3.hash(element, i) % self.size
            self.bit_array[hash_value] = True

    def contains(self, element):
        for i in range(self.num_hash_functions):
            hash_value = mmh3.hash(element, i) % self.size
            if not self.bit_array[hash_value]:
                return False
        return True
