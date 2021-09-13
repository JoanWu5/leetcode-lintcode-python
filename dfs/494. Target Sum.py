from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        self.memory = dict()
        self.dfs(nums, target, 0)
        return self.dfs(nums, target, 0)
    
    def dfs(self, nums, target, index):
        if (index, target) in self.memory:
            return self.memory[(index, target)]
        
        result = 0
        if index == len(nums):
            if target == 0:
                result = 1
        else:
            result = self.dfs(nums, target - nums[index], index + 1) + self.dfs(nums, target + nums[index], index + 1)
        
        self.memory[(index, target)] = result
        return result