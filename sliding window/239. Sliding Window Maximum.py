from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return []
        
        queue = deque()
        result = []
        for i, num in enumerate(nums):
            while queue and nums[queue[-1]] < num:
                queue.pop()
            queue.append(i)
            if queue[0] == i - k:
                queue.popleft()
            if i >= k - 1:
                result.append(nums[queue[0]])
        return result
            