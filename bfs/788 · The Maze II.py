from collections import deque
import math


class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def __init__(self):
        self.length = math.inf
        self.visited = dict()
        self.exist = False

    def is_des(self, x, y, destination):
        return x == destination[0] and y == destination[1]
    
    def is_valid(self, maze, x, y):
        m = len(maze)
        n = len(maze[0])
        return 0<= x < m and 0<= y < n and maze[x][y] == 0

    def shortestDistance(self, maze, start, destination):
        # write your code here
        if not maze or not start or not destination:
            return -1
        self.bfs(maze, start, destination)
        return self.length if self.exist else -1

    def bfs(self, maze, start, destination):
        sx, sy = start
        queue = deque([(sx, sy, 0)])
        self.visited[(sx, sy)] = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue:
            x, y, length = queue.popleft()
            if self.is_des(x, y, destination):
                self.exist = True
                self.length = min(self.length, length)
                continue
            
            for dx, dy in directions:
                new_x, new_y = x, y
                step = 0
                while self.is_valid(maze, new_x + dx, new_y + dy):
                    new_x += dx
                    new_y += dy
                    step += 1
                if (new_x, new_y) not in self.visited or self.visited[(new_x, new_y)] > step + length:
                    self.visited[(new_x, new_y)] = step + length
                    queue.append((new_x, new_y, step + length))
    