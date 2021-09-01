from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        
        presum_dict = {0: 1}
        presum = 0
        count = 0
        
        for i, num in enumerate(nums):
            presum += num
            
            if presum - k in presum_dict:
                count += presum_dict[presum - k]
            
            presum_dict[presum] = presum_dict.get(presum, 0) + 1
        
        return count