from typing import List
import math

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        while left < right:
            mid = left + (right - left) // 2
            if self.countDivide(nums, mid) <= threshold:
                right = mid
            else:
                left = mid + 1
        return left
    
    def countDivide(self, nums: List[int], divisor: int) -> int:
        return sum([math.ceil(num / divisor) for num in nums])
            