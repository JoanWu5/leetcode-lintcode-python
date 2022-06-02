# O(n)
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        self.partition(nums, 0, len(nums) - 1, 0, 2)
        
    def partition(self, nums: List[int], left: int, right: int, pivot_left: int, pivot_right: int):
        current = left
        while current <= right:
            if nums[current] == pivot_left:
                nums[current], nums[left] = nums[left], nums[current]
                left += 1
                current += 1
            elif nums[current] == pivot_right:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1
        
            
            