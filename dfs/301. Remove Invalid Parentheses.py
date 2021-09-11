from typing import List


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return [""]
        
        result = []
        left_pair, right_pair = 0, 0
        for char in s:
            if char == '(':
                left_pair += 1
            elif char == ')':
                right_pair  = right_pair + 1 if left_pair == 0 else right_pair
            
                left_pair = left_pair - 1 if left_pair > 0 else left_pair
                
        result = {}
        self.dfs(s, 0, 0, 0, left_pair, right_pair, [], result)
        return list(result.keys())
    
    def dfs(self, s, index, left_count, right_count, left_pair, right_pair, expression, result):
        if index == len(s):
            if left_pair == right_pair == 0:
                ans = ''.join(expression)
                result[ans] = 1
            return
            
        if (s[index] == '(' and left_pair > 0) or (s[index] == ')' and right_pair > 0):
            self.dfs(s, index + 1, left_count, right_count, left_pair - (s[index] == '('), right_pair - (s[index] == ')'), expression, result)
        
        expression.append(s[index])
        
        if s[index] != '(' and s[index] != ')':
            self.dfs(s, index + 1, left_count, right_count, left_pair, right_pair, expression, result)
        elif s[index] == '(':
            self.dfs(s, index + 1, left_count + 1, right_count, left_pair, right_pair, expression, result)
        elif s[index] == ')' and left_count > right_count:
            self.dfs(s, index + 1, left_count, right_count + 1, left_pair, right_pair, expression, result)
        
        expression.pop()
        
    