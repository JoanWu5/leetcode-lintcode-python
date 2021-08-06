# Implement an upper method to convert all characters in a string to uppercase.
# The characters not in alphabet don't need to convert.

# Example:
# Input: str = "abc"
# Output: "ABC"

class Solution:
    """
    @param str: A string
    @return: A string
    """
    def lowercaseToUppercase2(self, str):
        # write your code here
        result = ""
        for char in str:
            if 'a' <= char <= 'z':
                char = chr(ord(char) - ord('a') + ord('A'))
            result += char
        return result