from typing import List
import math

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums or sum(nums) < target:
            return 0
        
        left = 0
        min_size_subarray = math.inf
        left2right_sum = 0
        
        for right in range(len(nums)):
            left2right_sum += nums[right]
            if left2right_sum >= target and left <= right:
                while left2right_sum >= target:
                    min_size_subarray = min(min_size_subarray, right - left + 1)
                    left2right_sum -= nums[left]
                    left += 1
                    
        return 0 if min_size_subarray == math.inf else min_size_subarray