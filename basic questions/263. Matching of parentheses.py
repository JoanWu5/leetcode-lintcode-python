# Given a string containing just the characters '(', ')', determine if the input string is valid.

# The brackets must close in the correct order, "()" and "()" are all valid but "(]" and ")(" are not.

# Example:
# Input: ")("
# Output: False

class Solution:
    """
    @param string: A string
    @return: whether the string is a valid parentheses
    """
    def matchParentheses(self, string):
        # write your code here
        if len(string) == 0:
            return True
        matched = 0
        for char in string:
            if char == '(':
                matched += 1
            elif char == ')':
                matched -= 1
                if matched < 0:
                    return False
        return True
        