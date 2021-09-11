from typing import List
from collections import Counter


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        result = []
        frequencyMap = Counter(nums)
        n = len(nums)
        keys = list(frequencyMap.keys())
        self.dfs(n, [], 0, keys, frequencyMap, result)
        return result
    
    def dfs(self, n, path, index, keys, frequencyMap, result):
        result.append(list(path))
        
        if len(path) == n:
            return
        
        for i in range(index, len(keys)):
            num = keys[i]
            if frequencyMap[num] == 0:
                continue
                
            frequencyMap[num] -= 1
            path.append(num)
            self.dfs(n, path, i, keys, frequencyMap, result)
            path.pop()
            frequencyMap[num] += 1


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        result = []
        nums.sort()
        self.dfs(nums, [], 0, result)
        return result
    
    def dfs(self, nums, path, index, result):
        result.append(list(path))
        
        if len(path) == len(nums):
            return
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            
            path.append(nums[i])
            self.dfs(nums, path, i + 1, result)
            path.pop()