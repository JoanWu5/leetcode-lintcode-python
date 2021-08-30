# O(N)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        water = 0
        
        while left < right:
            left_height, right_height = height[left], height[right]
            water = max(water, min(left_height, right_height) * (right - left))
            if left_height < right_height:
                left += 1
            else:
                right -= 1
                 
        return water
                