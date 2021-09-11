from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        visited = set()
        self.helper(nums,visited,path,result)
        return result
    
    def helper(self,nums,visited,path,result):
        if len(path) == len(nums):
            result.append(path.copy())
        for i in range(len(nums)):
            if i not in visited:
                visited.add(i)
                path.append(nums[i])
                self.helper(nums,visited,path,result)
                visited.remove(i)
                path.pop()

                
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        result = []
        self.recur(nums, [], result)
        return result
    
    def recur(self, nums, path, result):
        if not nums:
            result.append(path)
            return
        
        for i in range(len(nums)):
            self.recur(nums[: i] + nums[i + 1:], path + [nums[i]], result)
            