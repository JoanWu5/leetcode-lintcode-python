from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        
        pointer, start, end = 0, 0, len(nums) - 1
        while pointer <= end:
            if nums[pointer] == 0:
                nums[start], nums[pointer] = nums[pointer], nums[start]
                start += 1
                pointer += 1
            elif nums[pointer] == 1:
                pointer += 1
            else:
                nums[pointer], nums[end] = nums[end], nums[pointer]
                end -= 1
        
            
            