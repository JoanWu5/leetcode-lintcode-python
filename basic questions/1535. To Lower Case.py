# Implement function ToLowerCase() that has a string parameter str.
# And convert the uppercase letters in the string to lowercase letters, 
# and then return the new string.

# Example:
# Input: "Hello"
# Output: "hello"

class Solution:
    """
    @param str: the input string
    @return: The lower case string
    """
    def toLowerCase(self, str):
        # Write your code here
        result = ""
        for char in str:
            if 'A' <= char <= 'Z':
                char = chr(ord(char) + ord('a') - ord('A'))
            result += char
        return result

