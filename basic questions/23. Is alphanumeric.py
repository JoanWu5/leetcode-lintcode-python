# Given a character c,return ture if it is a letter or a number,otherwise return false.

# If you use Python, the input will be a string which has a length of 1.

# Example:
# Input:
# c = '1'
# Output:
# true

class Solution:
    """
    @param c: A character.
    @return: The character is alphanumeric or not.
    """
    def isAlphanumeric(self, c: str) -> bool:
        # write your code here
        return '0' <= c <= '9' or 'a' <= c <= 'z' or 'A' <= c <= 'Z'

    # 自带函数：
    # 函数 str.isdigit() 判断字符是否为数字，函数 str.isalpha() 判断字符是否为字母，函数 str.isalnum() 判断字符是否为数字字母组合