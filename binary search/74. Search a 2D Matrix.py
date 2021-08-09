from typing import List


class Solution:
    # O(M + N)
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
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        m = len(matrix)
        n = len(matrix[0])
        
        begin, end = 0, m * n - 1
        while begin <= end:
            mid = begin + (end - begin) // 2
            midValue = matrix[mid // n][mid % n]
            if midValue == target:
                return True
            elif midValue < target:
                begin = mid + 1
            else:
                end = mid - 1
        return False
            
    
    

