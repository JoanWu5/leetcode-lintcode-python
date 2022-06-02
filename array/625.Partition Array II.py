# O(n)
from typing import (
    List,
)

class Solution:
    """
    @param nums: an integer array
    @param low: An integer
    @param high: An integer
    @return: nothing
    """
    def partition2(self, nums: List[int], low: int, high: int):
        # write your code here
        if not nums or len(nums) <= 1:
            return
        left, right = 0, len(nums) - 1
        pointer = left
        while pointer <= right:
            if nums[pointer] < low:
                nums[left], nums[pointer] = nums[pointer], nums[left]
                left += 1
                pointer += 1
            elif nums[pointer] > high:
                nums[right], nums[pointer] = nums[pointer], nums[right]
                right -= 1
            else:
                pointer += 1

