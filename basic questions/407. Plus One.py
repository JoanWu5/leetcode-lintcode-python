# Given a non-negative number represented as an array of digits, plus one to the number.Returns a new array.
# The number is arranged according to the number of digits, with the highest digit at the top of the list.

# Example:
# Input: [1,2,3]
# Output: [1,2,4]

class Solution:
    """
    @param digits: a number represented as an array of digits
    @return: the result
    """
    def plusOne(self, digits):
        # write your code here
        flag = 1
        result = []
        for i in range(len(digits) - 1, -1, -1):
            add = flag + digits[i]
            flag = add // 10
            result.insert(0, add % 10)
        
        if flag:
            result.insert(0, flag)
        
        return result