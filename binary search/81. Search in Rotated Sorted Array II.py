# O(logn)
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        
        left, right = 0, len(nums) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid
            elif nums[mid] < nums[left]:
                if nums[mid] < target <= nums[right]:
                    left = mid
                else:
                    right = mid
            else:
                left += 1
        
        if nums[left] == target:
            return True
        if nums[right] == target:
            return True
        return False
        