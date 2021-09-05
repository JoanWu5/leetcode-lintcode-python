from collections import deque

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def __init__(self):
        self.visited = set()
        self.result = False

    def hasPath(self, maze, start, destination):
        # write your code here
        if not maze or not start or not destination:
            return False
        
        self.bfs(maze, start, destination)
        return self.result

    def is_des(self, x, y, destination):
        if x == destination[0] and y == destination[1]:
            return True

    def is_valid(self, x, y, maze):
        m = len(maze)
        n = len(maze[0])
        return  0<= x < m and 0<= y < n and maze[x][y] == 0

    def bfs(self, maze, start, destination):
        sx, sy = start
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque([start])

        while queue:
            sx, sy = queue.popleft()
            if self.is_des(sx, sy, destination):
                self.result = True
                return
            for dx, dy in directions:
                x, y = sx, sy
                while self.is_valid(x + dx, y + dy, maze):
                    x += dx
                    y += dy
                if (x, y) not in self.visited:
                    self.visited.add((x, y))
                    queue.append((x, y))

class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def __init__(self):
        self.visited = set()
        self.result = False

    def hasPath(self, maze, start, destination):
        # write your code here
        if not maze or not start or not destination:
            return False
        
        self.bfs(maze, start, destination)
        return self.result

    def is_des(self, x, y, destination):
        if x == destination[0] and y == destination[1]:
            return True

    def is_valid(self, x, y, maze):
        m = len(maze)
        n = len(maze[0])
        return  0<= x < m and 0<= y < n and maze[x][y] == 0

    def bfs(self, maze, start, destination):
        sx, sy = start
        if self.result or self.is_des(sx, sy, destination):
            self.result = True
            return
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in directions:
            x, y = sx, sy
            while self.is_valid(x + dx, y + dy, maze):
                x += dx
                y += dy
            if (x, y) not in self.visited:
                self.visited.add((x, y))
                self.bfs(maze, (x, y), destination)
                
                