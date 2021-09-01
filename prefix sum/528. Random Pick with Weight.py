import random
from typing import List

# O(N)
class Solution:

    def __init__(self, w: List[int]):
        if not w:
            return
        self.presum = w
        for i in range(1, len(w)):
            self.presum[i] += self.presum[i - 1]

    def pickIndex(self) -> int:
        if not self.presum:
            return -1
        
        random_pick = random.randint(1, self.presum[-1])
        for index, presum in enumerate(self.presum):
            if presum >= random_pick:
                return index

# O(logN)
class Solution:

    def __init__(self, w: List[int]):
        if not w:
            return
        self.presum = w
        for i in range(1, len(w)):
            self.presum[i] += self.presum[i - 1]

    def pickIndex(self) -> int:
        if not self.presum:
            return -1
        
        random_pick = random.randint(1, self.presum[-1])
        left, right = 0, len(self.presum) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if random_pick == self.presum[mid]:
                return mid
            elif random_pick < self.presum[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()