from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        
        result = []
        self.dfs(n, 0, 0, [], result)
        return result
    
    def dfs(self, n, left_pair, right_pair, path, result):
        if len(path) == 2 * n:
            result.append(''.join(list(path)))
            return
        
        if left_pair < n:
            path.append('(')
            self.dfs(n, left_pair + 1, right_pair, path, result)
            path.pop()
        
        if right_pair < left_pair:
            path.append(')')
            self.dfs(n, left_pair, right_pair + 1, path, result)
            path.pop()
            
            
        