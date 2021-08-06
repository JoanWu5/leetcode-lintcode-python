# Given a string of char array and an offset, rotate the string by offset in place. (from left to right).
# In different languages, str will be given in different ways. 
# In place means you should change strings in the function. You don't return anything.

# Example:
# Input:
# str = ""abcdefg"
# offset = 3

class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        # write your code here
        if len(str) == 0:
            return str
        n = len(str)
        offset = offset % n
        temp = str[:n-offset]
        str[:offset] = str[n-offset:]
        str[offset:] = temp