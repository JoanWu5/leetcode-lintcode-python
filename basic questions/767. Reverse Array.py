# Reverse the given array nums inplace.
# Inplace means you can't use extra space.

# Example:
# Input : nums = [1,2,5]
# Output : [5,2,1]

class Solution:
    """
    @param nums: a integer array
    @return: nothing
    """
    def reverseArray(self, nums):
        # write your code here
        left, right = 0, len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        