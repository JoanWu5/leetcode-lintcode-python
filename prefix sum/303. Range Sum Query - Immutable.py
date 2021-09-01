from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        if not self.nums:
            return None
        
        if right >= len(self.nums):
            return None
        
        result = 0
        for i in range(left, right + 1):
            result += self.nums[i]
        return result


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class NumArray:

    def __init__(self, nums: List[int]):
        if not nums:
            return
        self.preSum = nums
        for i in range(len(nums) - 1):
            self.preSum[i + 1] += self.preSum[i]
        

    def sumRange(self, left: int, right: int) -> int:
        if not self.preSum:
            return None
        
        if right >= len(self.preSum):
            return None
        
        if left == 0:
            return self.preSum[right]
        
        return self.preSum[right] - self.preSum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)