from typing import List


class Solution:
    # 两个while看起来不好读，改成下面2版本
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left_result, right_result = mid, mid
                while left_result >= 0 and nums[left_result] == nums[mid]:
                    left_result -= 1
                while right_result <= len(nums) - 1 and nums[right_result] == nums[mid]:
                    right_result += 1
                return [max(0, left_result + 1), min(right_result - 1, len(nums) - 1)]
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return [-1, -1]

    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        result[0] = self.findFirstIndex(nums, target)
        result[1] = self.findLastIndex(nums, target)
        return result
    
    def findFirstIndex(self, nums: List[int], target: int) -> int:
        index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                index = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index
    
    def findLastIndex(self, nums: List[int], target: int) -> int:
        index = -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                index = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return index

                
                