from typing import List

# dp: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        leftMaxWater = [0] * n
        rightMaxWater = [0] * n
        
        leftMax = 0
        rightMax = 0
        
        for i in range(n):
            leftMax = max(leftMax, height[i])
            leftMaxWater[i] = leftMax
        
        for i in range(n - 1, -1, -1):
            rightMax = max(rightMax, height[i])
            rightMaxWater[i] = rightMax
        
        trapWater = 0
        for i in range(n):
            trapWater += min(leftMaxWater[i], rightMaxWater[i]) - height[i]
        
        return trapWater

# two pointers: O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        water = 0
        left, right = 0, len(height) - 1
        
        left_max, right_max = 0, 0
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max <= right_max:
                water += left_max - height[left]
                left += 1
            else:
                water += right_max - height[right]
                right -= 1

        return water