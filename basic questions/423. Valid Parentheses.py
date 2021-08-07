# Description
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

# Example:
# Input: "([)]"
# Output: False


class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def isValidParentheses(self, s):
        # write your code here
        if s is None:
            return True
        stack =[]
        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                if not stack:
                    return False
                left_char = stack.pop()
                if char == ')' and left_char != '(':
                    return False
                if char == ']' and left_char != '[':
                    return False
                if char == '}' and left_char != '{':
                    return False
        
        return not stack
