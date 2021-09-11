from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < 1 or k == 0:
            return []
        
        result = []
        self.dfs(n, k, [], 1, result)
        return result
    
    def dfs(self, n, k, path, index, result):
        if len(path) == k:
            result.append(list(path))
            return
        
        for i in range(index, n + 1):
            path.append(i)
            self.dfs(n, k, path, i + 1, result)
            path.pop()
        
            