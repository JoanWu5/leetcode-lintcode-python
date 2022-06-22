# O(nlogm) where m = max(nums)
from typing import List
import math


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        if not nums:
            return 0

        left, right = 1, max(nums)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.getSum(nums, mid) > threshold:
                left = mid
            else:
                right = mid

        if self.getSum(nums, left) <= threshold:
            return left
        return right

    def getSum(self, nums: List[int], divisor: int) -> int:
        return sum(int(math.ceil(num / divisor)) for num in nums)
