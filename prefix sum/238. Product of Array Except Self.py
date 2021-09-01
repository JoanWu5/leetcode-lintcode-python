# O(N) space: O(N)
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        n = len(nums)
        dp_prefix = [0] * n
        dp_suffix = [0] * n
        
        dp_prefix[0] = nums[0]
        dp_suffix[-1] = nums[-1]
        
        for i in range(1, n):
            dp_prefix[i] = nums[i] * dp_prefix[i - 1]
        
        for i in range(n - 2, -1, -1):
            dp_suffix[i] = nums[i] * dp_suffix[i + 1]
        
        result = [0] * n
        for i in range(n):
            if i == 0:
                result[i] = dp_suffix[1]
            elif i == n - 1:
                result[i] = dp_prefix[-2]
            else:
                result[i] = dp_prefix[i - 1] * dp_suffix[i + 1]
        
        return result