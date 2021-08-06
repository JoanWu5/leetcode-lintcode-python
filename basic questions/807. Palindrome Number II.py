# Determines whether a binary representation of a non-negative integer n is a palindrome

class Solution:
    """
    @param n: non-negative integer n.
    @return: return whether a binary representation of a non-negative integer n is a palindrome.
    """
    def isPalindrome(self, n):
        # Write your code here
        binary_presentation = []
        while n > 0:
            binary_presentation.append(n % 2)
            n = n // 2
        
        length = len(binary_presentation)
        for i in range(length //2):
            if binary_presentation[i] != binary_presentation[length - 1 - i]:
                return False
        
        return True
