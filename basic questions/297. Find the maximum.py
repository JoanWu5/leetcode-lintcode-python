# Find the maximum of n numbers.

from typing import (
    List,
)

class Solution:
    """
    @param nums: the list of numbers
    @return: return the maximum number.
    """
    def maxNum(self, nums: List[int]) -> int:
        # write your code here
        return max(nums)