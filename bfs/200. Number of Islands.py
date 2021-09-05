from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in self.visited:
                    self.bfs(grid, (i, j))
                    count += 1
        
        return count
    
    def bfs(self, grid, start):
        queue = deque([start])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        
        while queue:
            sx, sy = queue.popleft()
            self.visited.add((sx, sy))
            for dx, dy in directions:
                x, y = sx + dx, sy + dy
                if 0 <= x < m and 0<= y < n and grid[x][y] == "1" and (x, y) not in self.visited:
                    queue.append((x, y))
                    self.visited.add((x, y))

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid[0]) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        count = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.bfs(grid, (i, j))
                    count += 1
        
        return count
    
    def bfs(self, grid, start):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m = len(grid)
        n = len(grid[0])
        sx, sy = start
        
        if sx < 0 or sx >= m or sy < 0 or sy >= n or grid[sx][sy] == "0":
            return
        
        grid[sx][sy] = "0"
        for dx, dy in directions:
            x = sx + dx
            y = sy + dy
            self.bfs(grid, (x, y))
        
            