class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthese_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char not in parenthese_map:
                stack.append(char)
            else:
                top_element = stack.pop() if stack else '#'
                if top_element != parenthese_map[char]:
                    return False
        
        return len(stack) == 0