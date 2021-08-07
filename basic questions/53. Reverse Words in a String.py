# Given an input string, reverse the string word by word.

# Example:
# Input:
# s = "the sky is blue"
# Output:
# "blue is sky the"

class Solution:
    """
    @param: s: A string
    @return: A string
    """
    def reverseWords(self, s):
        # write your code here
        if len(s) == 0:
            return s
        word_list = s.strip().split()
        return ' '.join(word_list[::-1])