from heapq import heappush, heappop
from typing import List

# O(NlogK)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance_heap = []
        for point in points:
            distance = self.getDistance(point)
            heappush(distance_heap, (-distance, point))
            if len(distance_heap) > k:
                heappop(distance_heap)

        result = []
        while distance_heap:
            result.append(heappop(distance_heap)[1])
        
        return result
    
    
    def getDistance(self, point: List[int]) -> int:
        return pow(point[0], 2) + pow(point[1], 2)