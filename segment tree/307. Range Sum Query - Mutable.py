# build: O(n), update/sum: O(logn)
from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * 2 * len(nums)
        self.buildTree(nums)
        
    def buildTree(self, nums: List[int]):
        for i in range(self.n, 2 * self.n):
            self.tree[i] = nums[i - self.n]
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        while index > 0:
            left = right = index
            if index % 2 == 0:
                right = index + 1
            else:
                left = index - 1
            
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index = index // 2

    def sumRange(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        sum_range = 0
        while left <= right:
            if left % 2 == 1:
                sum_range += self.tree[left]
                left += 1
            if right % 2 == 0:
                sum_range += self.tree[right]
                right -= 1
                
            left = left // 2
            right = right //2
        return sum_range
            


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)