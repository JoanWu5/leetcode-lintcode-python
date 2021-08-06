# Convert a lowercase character to uppercase.
# You can assmue that the input is always lowercase.

# Example:
# Input: 'a'
# Output: 'A'

class Solution:
    """
    @param character: a character
    @return: a character
    """
    def lowercaseToUppercase(self, character):
        # write your code here
        return chr(ord(character) - (ord('a') - ord('A')))
    
