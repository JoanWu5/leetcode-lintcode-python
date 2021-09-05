from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True
        
        indegree = dict()
        graph = []
        
        for i in range(numCourses):
            indegree[i] = 0
            graph.append([])
        
        for prerequisite in prerequisites:
            neighbor, node = prerequisite
            indegree[neighbor] += 1
            graph[node].append(neighbor)
        
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        result = []
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        return len(result) == numCourses