from heapq import heappush, heappop
from collections import Counter
from typing import List

# O(NlogK)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_map = Counter(nums)
        frequency_heap = []
        
        for key, value in frequency_map.items():
            heappush(frequency_heap, (value, key))
            if len(frequency_heap) > k:
                heappop(frequency_heap)
        
        result = []
        while frequency_heap:
            result.append(heappop(frequency_heap)[1])
        
        return result