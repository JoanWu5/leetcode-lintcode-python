# Given a number n, return the double factorial of the number.
# In mathematics, the product of all the integers from 1 up to some non-negative integer n that 
# have the same parity (odd or even) as n is called the double factorial.

# We guarantee that the result does not exceed long.
# n is a positive integer
# Example:
# Input: n = 5
# Output: 15
# Explanation:
# 5!! = 5 * 3 * 1 = 15

class Solution:
    """
    @param n: the given number
    @return:  the double factorial of the number
    """
    def doubleFactorial(self, n):
        # Write your code here
        result = 1
        for i in range(n, 0, -2):
            result *= i
        return result
            