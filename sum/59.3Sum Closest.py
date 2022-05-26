# O(n^2)
import math
from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def three_sum_closest(self, numbers: List[int], target: int) -> int:
        # write your code here
        if not numbers or len(numbers) < 3:
            return
        
        numbers.sort()
        result = math.inf

        for i in range(2, len(numbers)):
            if i > 2 and numbers[i] == numbers[i - 1]:
                continue
            
            result = self.two_sum_closest(numbers, 0, i - 1, target, numbers[i], result)
        
        return result
    
    def two_sum_closest(self, numbers: List[int], left: int, right: int, target: int, minus: int, result: int) -> int:
        while left < right:
            current_sum = numbers[left] + numbers[right] + minus
            if current_sum == target:
                return current_sum

            if current_sum < target:
                left += 1
            else:
                right -= 1
            
            if abs(target - current_sum) < abs(target - result):
                result = current_sum
        
        return result


        
