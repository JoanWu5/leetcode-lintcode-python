# Given two integers a and b, an operator, choices:
#     +, -, *, /
# Calculate a <operator> b.

# Example:
# Input:
# a = 1
# b = 2
# operator = +
# Output:
# 3

class Calculator:
    """
    @param a: An integer
    @param operator: A character, +, -, *, /.
    @param b: An integer
    @return: The result
    """
    def calculate(self, a, operator, b):
        # write your code here
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        else:
            return a // b
