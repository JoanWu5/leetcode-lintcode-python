# Given a string S, find the largest alphabetic character, whose both uppercase and lowercase appear in S. 
# The uppercase character should be returned. 
# If there is no such character, return "NO".
 
# Example:
# Input: S = "admeDCAB"
# Output: "D"

# Input: S = "adme"
# Output: "NO"

class Solution:
    """
    @param s: a string
    @return: a string
    """
    def largestLetter(self, s):
        # write your code here
        flag = [0 for _ in range(52)]
        gap = 26
        for char in s:
            if 'a' <= char <= 'z':
                position = ord(char) - ord('a')
                flag[position] = 1

            elif 'A' <= char <= 'Z':
                position = ord(char) - ord('A')
                flag[position + gap] = 1
        
        for i in range(len(flag) - 1, gap, -1):
            if flag[i] == flag[i - gap] == 1:
                return chr(ord('A') + i - gap)
        return "NO"
