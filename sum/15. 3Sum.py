# O(n^2) space: O(n) for sorting
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        result = []
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            twosum_result = self.twoSum(nums, -nums[index], index + 1, len(nums) - 1)
            if len(twosum_result) != 0:
                result.extend(twosum_result)
        
        return result
            
    
    def twoSum(self, nums: List[int], target: int, left: int, right: int) -> List[int]:
        twosum_result = []
        while left < right:
            current_sum = nums[left] + nums[right]
            if current_sum == target:
                twosum_result.append([nums[left], nums[right], -target])
                
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -=1
            elif current_sum > target:
                right -= 1
            else:
                left += 1
        
        return twosum_result

# hashmap O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        nums.sort()
        result = []
        for index in range(len(nums)):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            
            twosum_result = self.twoSum(nums, -nums[index], index + 1)
            if len(twosum_result) != 0:
                result.extend(twosum_result)
        
        return result
            
    def twoSum(self, nums: List[int], target: int, index: int) -> List[int]:
        num_dict = dict()
        twosum_result = []

        while index < len(nums):
            num = nums[index]
            if target - num in num_dict:
                twosum_result.append([num, target - num, -target])
                while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                    index += 1
            num_dict[num] = index
            index += 1
                
        return twosum_result

# when not allowed to use sorting, hashmap: O(n^2)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []
        
        result = set()
        uniques = set()
        num_dict = dict()
        
        for i, val1 in enumerate(nums):
            if val1 not in uniques:
                uniques.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    target = -val1 - val2
                    if target in num_dict and num_dict[target] == i:
                        result.add(tuple(sorted((val1, val2, target))))
                    num_dict[val2] = i
        return result