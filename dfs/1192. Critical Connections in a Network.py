from collections import defaultdict
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if n <= 1:
            return []
        
        self.edges = defaultdict(list)
        for start, end in connections:            
            self.edges[start].append(end)
            self.edges[end].append(start)
            
        self.result = []
        self.visited = set()
        self.low = {}
        self.dfs(0, -1, 0)
        return self.result
    
    def dfs(self, id, pre_node, node):
        self.visited.add(node)
        self.low[node] = id
        
        for neighbor in self.edges[node]:
            if neighbor == pre_node:
                continue
            
            if neighbor not in self.visited:
                self.dfs(id + 1, node, neighbor)
            
            self.low[node] = min(self.low[node], self.low[neighbor])
            if id < self.low[neighbor]:
                self.result.append([node, neighbor])
        
        
                
                