# O(n)
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        appear_times = 1
        pointer = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[pointer - 1]:
                appear_times = 1
            else:
                appear_times += 1
            
            if appear_times <= 2:
                nums[pointer] = nums[i]
                pointer += 1
        
        return pointer