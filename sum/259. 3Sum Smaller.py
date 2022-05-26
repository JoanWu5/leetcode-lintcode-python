#O(n^2)
from typing import List


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) < 2:
            return 0
        
        nums.sort()
        result = 0
        
        for i in range(2, len(nums)):
            result += self.get2SumSmaller(nums, 0, i - 1, target - nums[i])
            
        return result
            
    def get2SumSmaller(self, nums: List[int], left: int, right: int, target: int) -> int:
        count = 0

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < target:
                count += right - left
                left += 1
            else:
                right -= 1
        
        return count
            
        