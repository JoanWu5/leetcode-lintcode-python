class Solution:
    def decodeString(self, s: str) -> str:
        result = ''
        stack = []
        current_string = ''
        operand = 0
        
        for char in s:
            if char.isdigit():
                operand = 10 * operand + int(char)
            elif char == '[':
                stack.append(current_string)
                stack.append(operand)
                
                operand = 0
                current_string = ''
            elif char == ']':
                num = stack.pop()
                prev_string = stack.pop()
                current_string = prev_string + num * current_string
                
            else:
                current_string += char
        
        return current_string