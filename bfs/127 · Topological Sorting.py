"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""

# dfs
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        
        result = []
        indegree = dict()
        for node in graph:
            indegree[node] = 0
        
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1
        
        for node in graph:
            if indegree[node] == 0:
                self.dfs(indegree, result, node)
        return result
        
    def dfs(self, indegree, result, node):
        result.append(node)
        indegree[node] -= 1
        for neighbor in node.neighbors:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                self.dfs(indegree, result, neighbor)
            

# bfs         
from collections import deque
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if not graph:
            return []
        
        result = []
        indegree = dict()
        for node in graph:
            indegree[node] = 0
        
        for node in graph:
            for neighbor in node.neighbors:
                indegree[neighbor] += 1
        
        queue = deque()
        for node in graph:
            if indegree[node] == 0:
                queue.append(node)
        
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in node.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return result       