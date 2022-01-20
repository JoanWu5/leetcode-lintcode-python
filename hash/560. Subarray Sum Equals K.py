from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_map = defaultdict(int)
        sum_map[0] = 1
        
        result = 0
        
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum - k in sum_map:
                result += sum_map[current_sum - k]
            sum_map[current_sum] += 1
        
        return result