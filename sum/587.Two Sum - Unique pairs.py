# O(nlogn)
from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of integer
    @param target: An integer
    @return: An integer
    """
    def two_sum6(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums or len(nums) < 2:
            return 0
        
        nums.sort()
        
        result = 0
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                result += 1
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
        
        return result