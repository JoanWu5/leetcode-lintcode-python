from collections import deque, defaultdict


class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # write your code here
        if n == 0 or len(edges) != n - 1:
            return False
        
        nodeMap = defaultdict(list)
        for node1, node2 in edges:
            nodeMap[node1].append(node2)
            nodeMap[node2].append(node1)
        
        queue = deque()
        visited = set()

        queue.append(0)
        visited.add(0)

        while queue:
            node = queue.popleft()
            for neighbor in nodeMap[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        
        return len(visited) == n