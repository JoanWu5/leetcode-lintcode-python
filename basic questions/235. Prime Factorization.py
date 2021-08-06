# Prime factorize a given integer.
# You should sort the factors in ascending order.

# Example:
# Input: 10
# Output: [2, 5]

import math

class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        # write your code here
        up = int(math.sqrt(num)) + 1
        f = [0 for _ in range(up)]
        prime = []
        for i in range(2, up):
            if f[i] == 0:
                prime.append(i)
                for j in range(i * i, up, i):
                    f[j] = 1
        
        result = []
        for a in prime:
            while num % a == 0:
                num = num // a
                result.append(a)
        
        if num != 1:
            result.append(num)
        return result