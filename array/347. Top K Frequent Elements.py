from heapq import *
from typing import List

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
        