# O(n * logm) where m = max(piles)
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if not piles or len(piles) > h:
            return 0

        left, right = 1, max(piles)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.getBananaHours(piles, mid) > h:
                left = mid
            else:
                right = mid

        if self.getBananaHours(piles, left) <= h:
            return left
        return right

    def getBananaHours(self, piles: List[int], speed: int) -> int:
        hours = 0
        for banana in piles:
            hours += int(math.ceil(banana / speed))
        return hours
