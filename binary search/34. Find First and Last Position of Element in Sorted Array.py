#O(logn)
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        result = []
        result.append(self.findFirstIndex(nums, 0, len(nums) - 1, target))
        result.append(self.findLastIndex(nums, 0, len(nums) - 1, target))
        return result
        
    def findFirstIndex(self, nums: List[int], left: int, right: int, target: int) -> int:      
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        return -1
    
    def findLastIndex(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left + 1 < right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        if nums[right] == target:
            return right
        if nums[left] == target:
            return left
        return -1

                
                