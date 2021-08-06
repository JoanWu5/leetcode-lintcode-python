# Given an integer n, return the first n-line Yang Hui triangle.

# 1.0<=n<=20
# 2.Yang Hui’s Triangle also called Pascal's triangle. --(Wikipedia)

# Example:
# Input : n = 4
# Output :  
# [
#  [1]
#  [1,1]
#  [1,2,1]
#  [1,3,3,1]
# ]


class Solution:
    """
    @param n: a Integer
    @return: the first n-line Yang Hui's triangle
    """
    def calcYangHuisTriangle(self, n):
        # write your code here
        result = []
        for i in range(n):
            line = [1 for _ in range(i + 1)]
            if i > 1:
                for j in range(1, i):
                    line[j] = result[i - 1][j - 1] + result[i - 1][j]
        
            result.append(line)
        return result

