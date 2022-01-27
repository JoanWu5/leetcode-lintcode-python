class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        first_pass_chars = []
        balance = 0
        open_char = 0
        
        for char in s:
            if char == '(':
                balance += 1
                open_char += 1
            if char == ')':
                if balance == 0:
                    continue
                balance -= 1
            first_pass_chars.append(char)
        
        result = []
        open_keep = open_char - balance
        for char in first_pass_chars:
            if char == '(':
                open_keep -= 1
                if open_keep < 0:
                    continue
            result.append(char)
        
        return ''.join(result)