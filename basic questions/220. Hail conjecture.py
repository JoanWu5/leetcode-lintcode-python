# Mathematicians have put forward a famous conjecture —— hail conjecture.
# For any natural number n, if n is even, replace n with n / 2;
# If n is odd, replace n with 3 * n + 1.
# According to this rule, the final result must be 1.
# How many times will the number change to 1?

class Solution:
    """
    @param num: an integer
    @return: return an integer
    """
    def getAnswer(self, num):
        # write your code here.
        result = 0
        while num > 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num = 3 * num + 1
            result += 1
        return result
