from collections import deque


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        if not words:
            return ""

        vertices = []
        graph = dict()
        indegree = dict()
        result = []

        for char in words[0]:
            vertices.append(char)

        for i in range(1, len(words)):
            for char in words[i]:
                vertices.append(char)
            diff_index = self.diff(words[i - 1], words[i])
            if diff_index == -2:
                return ""
            if diff_index != -1:
                node, neighbor = words[i - 1][diff_index], words[i][diff_index]
                if node not in graph:
                    graph[node] = []
                graph[node].append(neighbor)
        
        vertices = list(set(vertices))
        for node, neighbors in graph.items():
            graph[node] = list(set(neighbors))
        
        for vertice in vertices:
            indegree[vertice] = 0
            if vertice not in graph:
                graph[vertice] = []
        
        for node in graph.keys():
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        order = []
        for vertice in vertices:
            if indegree[vertice] == 0:
                order.append(vertice)
        
        order.sort()
        queue = deque(order)
        
        while queue:
            node = queue.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
            order = list(queue)
            order.sort()
            queue = deque(order)

        return "".join(result) if len(result) == len(vertices) else ""

            
    
    def diff(self, word1, word2):
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            if word1[i] != word2[i]:
                break
        
        if word1[i] == word2[i]:
            if len(word1) <= len(word2):
                return -1
            if len(word1) > len(word2):
                return -2
        return i


import heapq
# avoid sorting very time
class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code here
        if not words:
            return ""

        graph = dict()
        indegree = dict()
        result = []

        for word in words:
            for char in word:
                indegree[char] = 0
                graph[char] = []

        for i in range(1, len(words)):
            diff_index = self.diff(words[i - 1], words[i])
            if diff_index == -2:
                return ""
            if diff_index != -1:
                node, neighbor = words[i - 1][diff_index], words[i][diff_index]
                graph[node].append(neighbor)
        

        for node, neighbors in graph.items():
            graph[node] = list(set(neighbors))
        
        for node in graph.keys():
            for neighbor in graph[node]:
                indegree[neighbor] += 1

        heap = []
        for vertice in indegree.keys():
            if indegree[vertice] == 0:
                heap.append(vertice)
        
        heapq.heapify(heap)
        
        while heap:
            node = heapq.heappop(heap)
            result.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    heapq.heappush(heap, neighbor)

        return "".join(result) if len(result) == len(indegree) else ""

            
    
    def diff(self, word1, word2):
        min_length = min(len(word1), len(word2))
        for i in range(min_length):
            if word1[i] != word2[i]:
                break
        
        if word1[i] == word2[i]:
            if len(word1) <= len(word2):
                return -1
            if len(word1) > len(word2):
                return -2
        return i
