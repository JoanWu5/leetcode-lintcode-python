# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', 
# return the length of last word in the string.
# If the last word does not exist, return 0.
# A word is defined as a character sequence consists of non-space characters only.

# Example:
# Input: "Hello World"
# Output: 5

class Solution:
    """
    @param s: A string
    @return: the length of last word
    """
    def lengthOfLastWord(self, s):
        # write your code here
        word_list = s.strip().split(' ')
        return len(word_list[-1])