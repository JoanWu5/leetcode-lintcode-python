# O(n)
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        if not numbers or len(numbers) <= 1:
            return [-1, -1]

        left, right = 0, len(numbers) - 1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                return [left + 1, right + 1]

            if current_sum > target:
                right -= 1
            else:
                left += 1

        return [-1, -1]
