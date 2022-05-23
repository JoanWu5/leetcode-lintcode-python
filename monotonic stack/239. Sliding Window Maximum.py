from typing import List
from collections import deque


# deque: O(N) space: O(N)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k == 0:
            return 0

        if k == 1:
            return nums

        def clean_deque(i):
            if queue and queue[0] == i - k:
                queue.popleft()

            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

        queue = deque()
        max_index = 0
        for i in range(k):
            clean_deque(i)
            queue.append(i)
            if nums[i] > nums[max_index]:
                max_index = i

        output = [nums[max_index]]
        for i in range(k, len(nums)):
            clean_deque(i)
            queue.append(i)
            output.append(nums[queue[0]])

        return output
