# Given you two strings which are only contain digit character. You need to return a string spliced by the sum of the bits.

# A and B are strings which are composed of numbers
# Example:
# Input:
# A = "99"
# B = "111"
# Output: "11010"
# Explanation: because 9 + 1 = 10, 9 + 1 = 10, 0 + 1 = 1

class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return the sum of two strings
    """
    def SumofTwoStrings(self, A, B):
        # write your code here
        result = ""
        min_length = min(len(A), len(B))
        for i in range(min_length):
            result = str(int(A[len(A) - 1 - i]) + int(B[len(B) - 1 - i])) + result
        
        if i < len(A) - 1:
            result = A[:len(A) - 1 - i] + result
        
        if i < len(B) - 1:
            result = B[:len(B) - 1 - i] + result
        
        return result