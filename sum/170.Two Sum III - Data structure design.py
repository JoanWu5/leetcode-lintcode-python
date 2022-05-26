# add: O(1) find: O(n)
from collections import defaultdict


class TwoSum:

    def __init__(self):
        self.nums_dict = defaultdict(int)

    def add(self, number: int) -> None:
        self.nums_dict[number] += 1

    def find(self, value: int) -> bool:        
        for num in self.nums_dict.keys():
            if (value - num != num and value - num in self.nums_dict) or (value - num == num and self.nums_dict[num] >= 2):
                return True
    
        return False



# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)