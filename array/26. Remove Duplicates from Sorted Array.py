from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        start = 0
        for pointer in range(1, len(nums)):
            if nums[pointer] != nums[start]:
                start += 1
                nums[start] = nums[pointer]
                
        return start + 1
        