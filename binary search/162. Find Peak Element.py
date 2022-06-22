# O(logn)
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid
            elif nums[mid] < nums[mid - 1]:
                right = mid
            else:
                return mid

        if nums[left] >= nums[right]:
            return left
        return right
