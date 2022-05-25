# # O(n^(k - 1))
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
             we will sort your return value in output
    """
    def k_sum_i_i(self, a: List[int], k: int, target: int) -> List[List[int]]:
        # write your code here
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            if not nums or nums[0] * k > target or nums[-1] * k < target:
                return []

            if k == 1:
                for num in a:
                    if num == target:
                        return [[num]]
                return []

            if k == 2:
                return twoSum(nums, target)

            result = []

            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue

                for subset in kSum(nums[i + 1:], target - nums[i], k - 1):
                    result.append([nums[i]] + subset)
            return result

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            result = []
            left, right = 0, len(nums) - 1

            while left < right:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.append([nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif current_sum > target:
                    right -= 1
                else:
                    left += 1

            return result
        
        a.sort()
        return kSum(a, target, k)