from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return
        
        start = 0
        k = 2
        for pointer in range(len(nums)):
            if start < k or nums[pointer] > nums[start - k]:
                nums[start] = nums[pointer]
                start += 1
                
        return start