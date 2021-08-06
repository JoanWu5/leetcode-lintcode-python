class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        flag = 1 if number > 0 else -1
        number = abs(number)
        result = 0

        while number >= 1:
            left = number % 10
            number = number // 10
            result = result * 10 + left

        return result * flag