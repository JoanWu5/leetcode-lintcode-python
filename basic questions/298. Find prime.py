# Output all prime numbers within n.
# We promise that n is an integer within 100.

# Example:
# Input：5
# Output：[2, 3, 5]

class Solution:
    """
    @param n: an integer
    @return: return all prime numbers within n.
    """
    def prime(self, n):
        # write your code here
        result = []
        for i in range(2, n + 1):
            if self.is_prime(i):
                result.append(i)
        return result

    def is_prime(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        
        return True