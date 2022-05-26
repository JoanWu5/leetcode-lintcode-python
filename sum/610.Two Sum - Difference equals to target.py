from typing import (
    List,
)

class Solution:
    """
    @param nums: an array of Integer
    @param target: an integer
    @return: [num1, num2] (index1 < index2)
    """
    def two_sum7(self, nums: List[int], target: int) -> List[int]:
        # write your code here
        if not nums or len(nums) < 2:
            return
        
        target = abs(target)
        left, right = 0, 1
        while left < right and right < len(nums):
            current_minus = nums[right] - nums[left]
            if current_minus == target:
                return [nums[left], nums[right]]
            
            if current_minus < target:
                right += 1
            else:
                left += 1
                if left == right:
                    right += 1
        
        return