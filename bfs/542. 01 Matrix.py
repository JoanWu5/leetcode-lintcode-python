from collections import deque
import math
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or len(mat[0]) == 0:
            return []
        
        m = len(mat)
        n = len(mat[0])
        result = [[math.inf] * n for _ in range(m)]
        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                    queue.append((i, j))
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            sx, sy = queue.popleft()
            for dx, dy in directions:
                x, y = sx + dx , sy + dy
                if self.is_valid(x, y, mat) and result[x][y] > result[sx][sy] + 1:
                    result[x][y] = result[sx][sy] + 1
                    queue.append((x, y))

        return result
    
    def is_valid(self, x, y, mat):
        m = len(mat)
        n = len(mat[0])
        return 0<= x < m and 0<= y < n and mat[x][y] == 1


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or len(mat[0]) == 0:
            return []
        
        m = len(mat)
        n = len(mat[0])
        result = [[math.inf] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    result[i][j] = 0
                else:
                    if i > 0:
                        result[i][j] = min(result[i][j], result[i - 1][j] + 1)
                    if j > 0:
                        result[i][j] = min(result[i][j], result[i][j - 1] + 1)
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    result[i][j] = min(result[i][j], result[i + 1][j] + 1)
                if j < n - 1:
                    result[i][j] = min(result[i][j], result[i][j + 1] + 1)
        
        return result
            
        