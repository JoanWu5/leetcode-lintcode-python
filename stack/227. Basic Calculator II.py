class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operation = '+'
        operand = 0
        
        for index, char in enumerate(s):
            if char.isdigit():
                operand = 10 * operand + int(char)
            
            if index == len(s) - 1 or (not char.isdigit() and char != ' '):  
                if operation == '+':
                    stack.append(operand)
                elif operation == '-':
                    stack.append(-operand)
                elif operation == '*':
                    stack.append(stack.pop() * operand)
                elif operation == '/':
                    top_element = stack.pop()
                    if top_element // operand < 0 and top_element % operand != 0:
                        stack.append(top_element // operand + 1)
                    else:
                        stack.append(top_element // operand)
                    

                operand = 0
                operation = char
            
        return sum(stack)
        