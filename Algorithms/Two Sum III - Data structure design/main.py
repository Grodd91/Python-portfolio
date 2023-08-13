class TwoSum:
    def __init__(self):
        self.num_count = {}

    def add(self, num):
        if num in self.num_count:
            self.num_count[num] += 1
        else:
            self.num_count[num] = 1

    def find(self, target):
        for num in self.num_count:
            complement = target - num
            if complement == num and self.num_count[num] > 1:
                return True
            elif complement != num and complement in self.num_count:
                return True
        return False
