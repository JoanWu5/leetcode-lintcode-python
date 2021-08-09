from typing import List


class Solution:
    # 我这属于方法二，但是没提函数写的好难看,优化见search3
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or (len(nums) == 1 and nums[0] != target):
            return -1
        if len(nums) == 1 and nums[0] == target:
            return 0
        
        left, right = 0, len(nums) - 1
        has_pivot = False
        for pivot in range(len(nums) - 1):
            if nums[pivot] > nums[pivot + 1]:
                has_pivot = True
                break
        
        if has_pivot:
            if nums[0] <= target <= nums[pivot]:
                left, right = 0, pivot
            elif nums[pivot + 1] <= target <= nums[-1]:
                left, right = pivot + 1, len(nums) - 1
            else:
                return -1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

    def search3(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        pivotIndex = self.findPivot(nums, 0, len(nums) - 1)

        end = len(nums) - 1
        pivot = nums[pivotIndex]
        if target == pivot:
            return pivotIndex
        elif pivot < target <= nums[end]:
            return self.binary_search(nums, pivotIndex + 1, end, target)
        else:
            return self.binary_search(nums, 0, pivotIndex - 1, target)
    
    def findPivot(self, nums: List[int], start: int, end: int) -> int:
        if start == end:
            return start
        mid = start + (end - start) // 2
        if nums[mid] > nums[mid + 1]:
            return mid + 1
        elif nums[start] < nums[mid]:
            return self.findPivot(nums, mid + 1, end)
        else:
            return self.findPivot(nums, start, mid)
    
    def binary_search(self, nums: List[int], left: int, right: int, target: int) -> int:
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
                