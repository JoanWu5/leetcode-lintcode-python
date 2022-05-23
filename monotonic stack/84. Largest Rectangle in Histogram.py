from typing import List
import math


# brute force: O(N^2), space: O(1)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            min_height = math.inf
            for j in range(i, len(heights)):
                min_height = min(min_height, heights[j])
                max_area = max(max_area, min_height * (j - i + 1))
        return max_area


# divide and conquer: O(NlogN), worst case: O(N^2), space: O(N)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.calculateArea(heights, 0, len(heights) - 1)

    def calculateArea(self, heights: List[int], start: int, end: int) -> int:
        if start > end:
            return 0

        min_height_index = start
        for i in range(start, end + 1):
            if heights[min_height_index] > heights[i]:
                min_height_index = i

        return max(heights[min_height_index] * (end - start + 1),
                   self.calculateArea(heights, start, min_height_index - 1),
                   self.calculateArea(heights, min_height_index + 1, end))


# stack: O(N) space: O(N)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        max_area = 0
        for i in range(len(heights)):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
                current_height = heights[stack.pop()]
                current_width = i - stack[-1] - 1
                max_area = max(max_area, current_height * current_width)
            stack.append(i)

        while stack[-1] != -1:
            current_height = heights[stack.pop()]
            current_width = len(heights) - stack[-1] - 1
            max_area = max(max_area, current_height * current_width)

        return max_area
