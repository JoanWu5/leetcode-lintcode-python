from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        result = []
        num_frequency = Counter(nums)
        path = []
        self.dfs(nums, path, num_frequency, result)
        return result
        
    def dfs(self, nums, path, num_frequency, result):
        if len(path) == len(nums):
            result.append(list(path))
            return
        
        for num in num_frequency.keys():
            if num_frequency[num] > 0:
                num_frequency[num] -= 1
                path.append(num)
                self.dfs(nums, path, num_frequency, result)
                path.pop()
                num_frequency[num] += 1
        