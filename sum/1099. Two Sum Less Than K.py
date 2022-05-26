# O(nlogn)
from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return -1

        nums.sort()

        left, right = 0, len(nums) - 1
        result = -1
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum < k:
                result = max(result, current_sum)
                left += 1
            else:
                right -= 1

        return result
