from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if self.canEatingAll(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        return left
     
    def canEatingAll(self, piles: List[int], h: int, speed: int) -> bool:
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours <= h


                