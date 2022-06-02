from heapq import *
from typing import List

# O(nlogk)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums or k > len(nums):
            return []
        
        frequencyMap = dict()
        for num in nums:
            frequencyMap[num] = frequencyMap.get(num, 0) + 1
        
        minheap = []
        for num, frequency in frequencyMap.items():
            if len(minheap) < k:
                heappush(minheap, (frequency, num))    
            else:
                if frequency > minheap[0][0]:
                    heappop(minheap)
                    heappush(minheap, (frequency, num))
        
        result = []       
        while minheap:
            frequency, num = heappop(minheap)
            result.append(num)
    
        return result

# average: O(N) worst: O(N^2)
from collections import Counter
import random


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        
        num_frequency = Counter(nums)
        num_frequency_list = list(num_frequency.items())
        n = len(num_frequency_list)
        self.select(num_frequency_list, n - k, 0, n - 1)
        result = []
        for i in range(n - 1, n - k - 1, -1):
            result.append(num_frequency_list[i][0])
        
        return result
    
    def partition(self, nums: List[tuple], left: int, right: int):
        pivotIndex = random.randint(left, right)
        pivot = nums[pivotIndex][1]
        
        nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]
        midIndex = left
        
        for pointer in range(left, right):
            if nums[pointer][1] <= pivot:
                nums[midIndex], nums[pointer] = nums[pointer], nums[midIndex]
                midIndex += 1
        
        nums[midIndex], nums[right] = nums[right], nums[midIndex]
        return midIndex
    
    def select(self, nums: List[tuple], k_smallest: int, left: int, right: int):
        if left >= right:
            return
        
        split = self.partition(nums, left, right)
        if split >= k_smallest:
            self.select(nums, k_smallest - 1, left, split - 1)
            return
        
        self.select(nums, k_smallest, split + 1, right)