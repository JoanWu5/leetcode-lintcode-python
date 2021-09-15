from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        numMap = dict()
        result = []
        for num in nums:
            if num in numMap:
                result.append(num)
            else:
                numMap[num] = 1
        
        return result

# O(1) space
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        result = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                result.append(abs(num))
            else:
                nums[abs(num) - 1] *= -1
        return result

class Solution:
    def findDuplicates(self, nums):
        if not nums:
            return []
        for i in range(len(nums)):
            while i != nums[i] - 1 and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        return [nums[it] for it in range(len(nums)) if it != nums[it] - 1]