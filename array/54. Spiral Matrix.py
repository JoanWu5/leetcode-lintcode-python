from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or len(matrix[0]) == 0:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        result = []
        left, right, low, high = 0, n - 1, 0, m - 1
        while left <= right and low <= high:
            if left > right:
                break
            for col in range(left, right + 1):
                    result.append(matrix[low][col])

            low += 1
            if low > high:
                break
            for row in range(low, high + 1):
                result.append(matrix[row][right])

            right -= 1
            if left > right:
                break
            for col in range(right, left - 1, -1):
                result.append(matrix[high][col])

            high -= 1
            if low > high:
                break
            for row in range(high, low - 1, -1):
                result.append(matrix[row][left])

            left += 1
        
        return result