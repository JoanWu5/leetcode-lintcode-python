from collections import deque
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        if not rooms or len(rooms) == 0:
            return True
        
        queue = deque()
        visited = set()
        
        queue.append(0)
        visited.add(0)
        
        while queue:
            room = queue.popleft()
            for key in rooms[room]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
        
        return len(visited) == len(rooms)
        
        