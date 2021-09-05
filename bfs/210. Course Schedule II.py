from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []
        
        result = []
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
        
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result if len(result) == numCourses else []