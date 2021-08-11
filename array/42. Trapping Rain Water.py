from typing import List

# dp
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

# two pointers
class Solution2:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left, right = 0, n - 1
        l_max, r_max = 0, 0
        trapWater = 0
        
        while left < right:
            l_max = max(l_max, height[left])
            r_max = max(r_max, height[right])
            if l_max <= r_max:
                trapWater += l_max - height[left]
                left += 1
            else:
                trapWater += r_max - height[right]
                right -= 1
        
        return trapWater