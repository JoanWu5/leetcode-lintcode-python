# Given a sentence of English, update the first letter of each word to uppercase.

# The given sentence may not be a grammatical sentence.
# The length of the sentence does not exceed 100.
# Example:
# Input: s =  "i want to get an accepted"
# Output: "I Want To Get An Accepted"

class Solution:
    """
    @param s: a string
    @return: a string after capitalizes the first letter
    """
    def capitalizesFirst(self, s):
        # Write your code here
        result = ""
        has_space = True
        for char in s:
            if char == ' ':
                has_space = True
            else:
                if has_space:
                    has_space = False
                    char = char.upper()
            
            result += char
        return result