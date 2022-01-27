class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        result = 0
        sign = 1
        
        for char in s:
            if char == ' ':
                continue
            
            if char.isdigit():
                operand = 10 * operand + int(char)
            elif char == '+':
                result += sign * operand
                
                sign = 1
                operand = 0
            elif char == '-':
                result += sign * operand
                
                sign = -1
                operand = 0
            elif char == '(':
                stack.append(result)
                stack.append(sign)
                sign = 1
                result = 0
            elif char == ')':
                result += sign * operand
                result *= stack.pop()
                result += stack.pop()
                
                operand = 0

        return result + sign * operand
            
            
            