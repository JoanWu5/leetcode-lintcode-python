from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        
    def is_valid(self, x, y, grid):
        rows = len(grid)
        cols = len(grid[0])
        return 0<= x < rows and 0<= y < cols and grid[x][y] == 1
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        exist = False
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    self.visited.add((i, j))
                elif grid[i][j] == 1:
                    exist = True
                
        if exist and len(queue) == 0:
            return -1
        
        if not exist and len(queue) == 0:
            return 0
        
        max_time = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            sx, sy, time = queue.popleft()
            max_time = max(max_time, time)
            for dx, dy in directions:
                x, y = sx + dx, sy + dy
                if self.is_valid(x, y, grid) and (x, y) not in self.visited:
                    self.visited.add((x, y))
                    queue.append((x, y, time + 1))
                    grid[x][y] = 2
        
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    return -1
        
        return max_time
                