class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        if not S or len(S) < 3:
            return 0
        
        S.sort()

        count = 0
        n = len(S)
        
        for i in range(len(S) - 1, -1, -1):
            start, end = 0, i - 1
            count += self.count_two(S[i], start, end, S)

        return count
        
    def count_two(self, c, start, end, S):
        count = 0
        while start < end:
            current_sum = S[start] + S[end] - c
            if current_sum > 0:
                count += end - start
                end -= 1
            else:
                start += 1
        
        return count