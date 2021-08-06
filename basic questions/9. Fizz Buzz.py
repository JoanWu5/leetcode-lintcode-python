# Given number n. Print number from 1 to n. According to following rules:

# when number is divided by 3, print "fizz".
# when number is divided by 5, print "buzz".
# when number is divided by both 3 and 5, print "fizz buzz".
# when number can't be divided by either 3 or 5, print the number itself.
# Example:
# Input:
# n = 15
# Output:
# [
#   "1", "2", "fizz",
#   "4", "buzz", "fizz",
#   "7", "8", "fizz",
#   "buzz", "11", "fizz",
#   "13", "14", "fizz buzz"
# ]

class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        # write your code here
        result = [str(i + 1) for i in range(n)]
        for i in range(1, n//3 + 1):
            result[3 * i - 1] = "fizz"
        
        for i in range(1, n//5 + 1):
            result[5 * i - 1] = "buzz"
        
        for i in range(1, n//15 + 1):
            result[15 * i - 1] = "fizz buzz"
        
        return result