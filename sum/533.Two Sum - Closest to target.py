# O(nlogn)
from typing import (
    List,
)
import math


class Solution:
    """
    @param nums: an integer array
    @param target: An integer
    @return: the difference between the sum and the target
    """
    def two_sum_closest(self, nums: List[int], target: int) -> int:
        # write your code here
        if not nums or len(nums) < 2:
            return

        nums.sort()

        result = math.inf
        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                return 0

            if current_sum < target:
                left += 1
            else:
                right -= 1
            
            if abs(target - current_sum) < result:
                result = abs(target - current_sum)
        
        return result