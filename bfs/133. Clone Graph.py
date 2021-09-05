# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        nodeMap = {node: Node(node.val)}
        
        queue = deque([node])
        while queue:
            newNode = queue.popleft()
            if newNode.neighbors:
                for neighbor in newNode.neighbors:
                    if neighbor not in nodeMap:
                        queue.append(neighbor)
                        nodeMap[neighbor] = Node(neighbor.val)
                    nodeMap[newNode].neighbors.append(nodeMap[neighbor])
        
        return nodeMap[node]
            

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        nodeMap = {}
        self.recursive(node, nodeMap)
        return nodeMap[node]
    
    def recursive(self, node, nodeMap):
        if node in nodeMap:
            return nodeMap[node]
        
        newNode = Node(node.val)
        nodeMap[node] = newNode
        
        for neighbor in node.neighbors:
            newNode.neighbors.append(self.recursive(neighbor, nodeMap))
          
        return newNode
                
            
            
            