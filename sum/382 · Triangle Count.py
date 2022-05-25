# O(n^2)
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
        result = 0

        for i in range(len(S)):
            left, right = 0, i - 1
            while left < right:
                current_sum = S[left] + S[right]
                if current_sum > S[i]:
                    result += right - left
                    right -= 1
                else:
                    left += 1
        
        return result
        