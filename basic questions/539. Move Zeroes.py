# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
# Example:
# Input: nums = [0, 1, 0, 3, 12],
# Output: [1, 3, 12, 0, 0].

class Solution:
    """
    @param nums: an integer array
    @return: nothing
    """
    def moveZeroes(self, nums):
        # write your code here
        non_zero_pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_pointer] = nums[i]
                non_zero_pointer += 1
        
        for i in range(non_zero_pointer, len(nums)):
            nums[i] = 0
        
        return nums