class Solution:
    """
    @param n: a integer
    @return: return a 2D array
    """
    def getFactors(self, n):
        # write your code here
        if n <= 1:
            return []
        
        result = []
        i = 2
        while i * i <= n:
            if n % i == 0:
                q = n // i
                result.append([i, q])
                subresult = self.getFactors(q)
                for r in subresult:
                    if r[0] >= i:
                        result.append([i] + r)
            i += 1
        return result