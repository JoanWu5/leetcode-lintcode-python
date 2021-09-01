from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
    
        num_dict = dict()
        
        for index, num in enumerate(nums):
            if target - num in num_dict:
                return [index, num_dict[target - num]]
            else:
                num_dict[num] = index
                
        return [-1, -1]
        