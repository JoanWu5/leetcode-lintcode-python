from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) <= 1:
            return []
        
        result = []
        self.dfs(nums, 0, [], result)
        return result
    
    def dfs(self, nums, index, path, result):
        if len(path) >= 2:
            result.append(list(path))
        
        if index == len(nums):
            return
        
        used = set()
        for i in range(index, len(nums)):
            if len(path) > 0 and path[-1] > nums[i]:
                continue
            if nums[i] in used:
                continue
            
            used.add(nums[i])
            path.append(nums[i])
            self.dfs(nums, i + 1, path, result)
            path.pop()
            
            
            
            
            
            