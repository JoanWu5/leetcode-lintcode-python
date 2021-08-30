from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        
        start, product, count = 0, 1, 0
        for end, num in enumerate(nums):
            product *= num
            while product >= k and start <= end:
                product //= nums[start]
                start += 1
            
            count += end - start + 1
        
        return count
        