from typing import List


class Solution:
    def valid(self, x, y, m, n, visited):
        if 0<= x <= m and 0<= y < n and (x, y) not in visited:
            return True
        
        return False
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix and len(matrix[0]) == 0:
            return
        
        
        rows = set()
        cols = set()
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for row in range(m):
            for col in range(n):
                if row in rows or col in cols:
                    matrix[row][col] = 0
                    
            
# matrix[0][0] 表示第一行有0
# is_col 表示第一列   
class Solution:
    def valid(self, x, y, m, n, visited):
        if 0<= x <= m and 0<= y < n and (x, y) not in visited:
            return True
        
        return False
    
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix and len(matrix[0]) == 0:
            return
        
        is_col = False
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
            
        
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
        
        if is_col:
            for i in range(m):
                matrix[i][0] = 0