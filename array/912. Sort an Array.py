import random
from typing import List


# quickSort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    
    def quickSort(self, nums: List[int], left: int, right: int) -> int:
        if left >= right:
            return 
        
        pivotIndex = random.randint(left, right)
        pivot = nums[pivotIndex]
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
        pointer = left
        for i in range(left, right):
            if nums[i] < pivot:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
        nums[pointer], nums[right] = nums[right], nums[pointer]
        self.quickSort(nums, left, pointer - 1)
        self.quickSort(nums, pointer + 1, right)

# mergeSort
class Solution2:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) == 1:
            return nums

        mid = len(nums) // 2
        leftPart = nums[:mid]
        rightPart = nums[mid:]
        self.sortArray(leftPart)
        self.sortArray(rightPart)
        left, right, pointer = 0, 0, 0
        while left < len(leftPart) and right < len(rightPart):
            if leftPart[left] < rightPart[right]:
                nums[pointer] = leftPart[left]
                left += 1
            else:
                nums[pointer] = rightPart[right]
                right += 1
            pointer += 1
        nums[pointer:] = leftPart[left:] + rightPart[right:]
        return nums
    
        