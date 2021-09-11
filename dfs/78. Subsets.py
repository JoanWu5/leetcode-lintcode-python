from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        result = []
        self.dfs(nums, 0, [], result)
        return result
    
    def dfs(self, nums, index, path, result):
        result.append(list(path))
        
        if index == len(nums):
            return
        
        for i in range(index, len(nums)):
            path.append(nums[i])
            self.dfs(nums, i + 1, path, result)
            path.pop()
    
    
        