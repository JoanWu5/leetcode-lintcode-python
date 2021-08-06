# Given a rotated sorted array, return it to sorted array in-place.（Ascending）
# What is rotated array?
# For example, the orginal array is [1,2,3,4], The rotated array of it can be [1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]

# Example:
# Input:
# array = [4,5,1,2,3]
# Output:
# [1,2,3,4,5]

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        n = len(nums)
        flag = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                flag = 1
                break
        if flag:
            temp = nums[:i+1]
            nums[:n-i-1] = nums[i+1:]
            nums[n-i-1:] = temp 

# in-place
class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        n = len(nums)
        flag = 0
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                flag = 1
                break
        if not flag:
            return

        self.reverse(nums, 0, i)
        self.reverse(nums, i + 1, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)
    
    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

