from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.visited = set()
        
    def is_valid(self, x, y, image, originColor):
        m = len(image)
        n = len(image[0])
        return 0<= x < m and 0<= y < n and image[x][y] == originColor
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or len(image[0]) == 0:
            return []
        
        m = len(image)
        n = len(image[0])
        if sr >=m or sc >= n:
            return []
        
        originColor = image[sr][sc]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                    
        queue = deque([(sr, sc)])
        self.visited.add((sr, sc))
        
        while queue:
            sx, sy = queue.popleft()
            image[sx][sy] = newColor
            for dx, dy in directions:
                x, y = sx + dx, sy + dy
                if self.is_valid(x, y, image, originColor) and (x, y) not in self.visited:
                    self.visited.add((x, y))
                    queue.append((x, y))
        
        return image
                    
class Solution:
    def is_valid(self, x, y, image, originColor):
        m = len(image)
        n = len(image[0])
        return 0<= x < m and 0<= y < n and image[x][y] == originColor
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if not image or len(image[0]) == 0:
            return []
        
        m = len(image)
        n = len(image[0])
        if sr >=m or sc >= n:
            return []
        
        originColor = image[sr][sc]
        if originColor == newColor:
            return image
        
        self.dfs(sr, sc, image, originColor, newColor)
        return image
    
    def dfs(self, r, c, image, originColor, newColor):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        image[r][c] = newColor
        
        for dx, dy in directions:
            x, y = r + dx, c + dy
            if self.is_valid(x, y, image, originColor):
                self.dfs(x, y, image, originColor, newColor)
                    
        