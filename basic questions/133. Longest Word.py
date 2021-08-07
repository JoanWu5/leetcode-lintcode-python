# Given a dictionary, find all of the longest words in the dictionary.

# Example:
# 	Input: {
# 		"dog",
# 		"google",
# 		"facebook",
# 		"internationalization",
# 		"blabla"
# 		}
# 	Output: ["internationalization"]

class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    def longestWords(self, dictionary):
        # write your code here
        result = []
        longest = 0
        for word in dictionary:
            if len(word) > longest:
                longest = len(word)
                result = [word]
            elif len(word) == longest:
                result.append(word)

        return result