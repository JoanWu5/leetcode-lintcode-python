# o(N)
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
       
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = nums[i]
            if dp[i - 1] > 0:
                dp[i] += dp[i - 1]
        
        return max(dp)
    
    