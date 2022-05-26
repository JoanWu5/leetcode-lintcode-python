from typing import (
    List,
)
# O(nlogn)
class Solution:
    """
    @param nums: an array of integer
    @param target: an integer
    @return: an integer
    """
    def two_sum5(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums:
            return 0
        
        nums.sort()
        
        result = 0
        left, right = 0, len(nums) - 1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum <= target:
                result += right - left
                left += 1
            else:
                right -= 1
        
        return result
