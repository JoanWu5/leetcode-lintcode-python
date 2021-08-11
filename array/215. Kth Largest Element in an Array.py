import random
from typing import List

#  O(NlogK) space: O(K)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or k > len(nums):
            return None
        largestIndex = len(nums) - k
        
        midIndex = self.partition(nums, 0, len(nums) - 1)
        if midIndex == largestIndex:
            return nums[midIndex]
        elif midIndex < largestIndex:
            return self.findKthLargest(nums[midIndex:], k)
        else:
            return self.findKthLargest(nums[:midIndex], k - (len(nums) - midIndex))
    
    def partition(self, nums: List[int], left: int, right: int) -> int:
        if left > right:
            return
        
        pivotIndex = random.randint(left, right)
        pivot = nums[pivotIndex]
        
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
        midIndex = left
        
        for pointer in range(left, right):
            if nums[pointer] <= pivot:
                nums[midIndex], nums[pointer] = nums[pointer], nums[midIndex]
                midIndex += 1
        
        nums[midIndex], nums[right] = nums[right], nums[midIndex]
        return midIndex

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
        
        