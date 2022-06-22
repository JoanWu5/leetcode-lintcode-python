from typing import List

# O(M + N)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        row, col = m - 1, 0
        while row >= 0 and col < n:
            currentValue = matrix[row][col]
            if currentValue == target:
                return True
            elif currentValue < target:
                col += 1
            else:
                row -= 1
        return False

# O(logM + logN)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        n, m = len(matrix), len(matrix[0])
        left, right = 0, n * m - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            mid_num = matrix[mid // m][mid % m]
            if mid_num == target:
                return True
            if mid_num > target:
                right = mid
            else:
                left = mid

        if matrix[left // m][left % m] == target:
            return True
        if matrix[right // m][right % m] == target:
            return True
        return False
    
    

