# Enter a positive integer 'N'. You need to return a list of strings as shown in the Example.
# Example
# Example 1:
# Input:
# n = 1
# Output:
# ["X"]
# Explanation:
# The answer list can be seen as the following shape:
# X

# Example 2:
# Input:
# n = 2
# Output:
# ["XX", "XX"]
# Explanation:
# The answer list can be seen as the following shape:
# XX
# XX

# Example 3:
# Input:
# n = 3
# Output:
# ["X X", " X ", "X X"]
# Explanation:
# The answer list can be seen as the following shape:
# X X
#  X 
# X X

# Example 4:
# Input:
# n = 4
# Output:
# ["X  X", " XX ", " XX ", "X  X"]
# Explanation:
# The answer list can be seen as the following shape:
# X  X 
#  XX  
#  XX 
# X  X

# Example 5:
# Input:
# n = 5
# Output:
# ["X   X", " X X ", "  X  ", " X X ", "X   X"]
# Explanation:
# The answer list can be seen as the following shape:
# X   X 
#  X X  
#   X   
#  X X  
# X   X 

class Solution:
    """
    @param n: An integer.
    @return: A string list.
    """
    def printX(self, n: int):
        # write your code here
        result = []
        for i in range(n):
            line_i = ""
            for j in range(n):
                if j == i or j == n - i - 1:
                   line_i += "X"
                else:
                    line_i += " "
            result.append(line_i)
        return result
