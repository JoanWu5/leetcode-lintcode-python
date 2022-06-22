# O(logn)
from typing import List

# two rounds, first find the minimum index, second find the target
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        smallest_index = self.findMinimum(nums)
        if target < nums[smallest_index]:
            return -1

        if nums[smallest_index] <= target <= nums[len(nums) - 1]:
            return self.binarySearch(nums, target, smallest_index, len(nums) - 1)
        return self.binarySearch(nums, target, 0, smallest_index)

    def findMinimum(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid

        if nums[left] <= nums[right]:
            return left
        return right

    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid
            else:
                right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1

# 1 round
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid

        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
