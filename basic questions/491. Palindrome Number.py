# Check a positive number is a palindrome or not.
# A palindrome number is that if you reverse the whole number you will get exactly the same number.


class Solution:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
        return str(num) == str(num)[::-1]


class Solution2:
    """
    @param num: a positive number
    @return: true if it's a palindrome or false
    """
    def isPalindrome(self, num):
        # write your code here
        return num == self.reverse_num(num)
    
    def reverse_num(self, num):
        result = 0
        while num > 0:
            result = 10 * result + num % 10
            num = num // 10
        return result