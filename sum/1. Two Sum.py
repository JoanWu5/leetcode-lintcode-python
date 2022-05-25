# O(n)
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
    
        num_dict = dict()
        
        for index, num in enumerate(nums):
            if target - num in num_dict:
                return [index, num_dict[target - num]]
            
            num_dict[num] = index
                
        return [-1, -1]

# O(nlogn) if the array is sorted, then O(n), better than hashmap since the space is O(1)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
    	
        nums = [(number, index) for index, number in enumerate(nums)]
        nums.sort()
        
        left, right = 0, len(nums) - 1
        while left < right:
            current = nums[left][0] + nums[right][0]
            if current > target:
                right -= 1
            elif current < target:
                left += 1
            else:
                return [nums[left][1], nums[right][1]]
                
        return [-1, -1]