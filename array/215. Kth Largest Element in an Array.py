import random
from typing import List

#  O(NlogK) space: O(K)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k <= 0 or k > len(nums):
            return
        
        return self.select(nums, len(nums) - k, 0, len(nums) - 1)
    
    def partition(self, nums: List[int], left: int, right: int) -> int:
        if left >= right:
            return left
    
        pivot_index = random.randint(left, right)
        pivot = nums[pivot_index]
        nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
        pointer = left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
                
        nums[right], nums[pointer] = nums[pointer], nums[right]
        return pointer
    
    def select(self, nums: List[int], k_smallest: int, left: int, right: int):
        split = self.partition(nums, left, right)
        if split == k_smallest:
            return nums[split]
        
        if split > k_smallest:
            return self.select(nums, k_smallest, left, split - 1)
        
        return self.select(nums, k_smallest, split + 1, right)

# quickSort O(N^2) space: O(N)    
import random

class Solution2:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k > len(nums):
            return []
        
        frequencyMap = dict()
        for num in nums:
            frequencyMap[num] = frequencyMap.get(num, 0) + 1
        uniqueKey = list(frequencyMap.keys())
        
        def partition(left: int, right: int, pivotIndex: int) -> int:
            pivotFrequency = frequencyMap[uniqueKey[pivotIndex]]
            uniqueKey[pivotIndex], uniqueKey[right] = uniqueKey[right], uniqueKey[pivotIndex]
            pointer = left
            for i in range(left, right):
                if frequencyMap[uniqueKey[i]] < pivotFrequency:
                    uniqueKey[pointer], uniqueKey[i] = uniqueKey[i], uniqueKey[pointer]
                    pointer += 1
            
            uniqueKey[pointer], uniqueKey[right] = uniqueKey[right], uniqueKey[pointer]
            return pointer
        
        def quickSelect(left: int, right: int, kSmallest: int) -> None:
            if left >= right:
                return
            
            pivotIndex = random.randint(left, right)
            pivotIndex = partition(left, right, pivotIndex)
            
            if kSmallest == pivotIndex:
                return
            elif kSmallest < pivotIndex:
                quickSelect(left, pivotIndex - 1, kSmallest)
            else:
                quickSelect(pivotIndex + 1, right, kSmallest)
        
        n = len(uniqueKey)
        quickSelect(0, n - 1, n - k)
        return uniqueKey[n - k:]
        
        