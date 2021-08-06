# Given an integers array A.

# Example:
# Input:
# A = [1,2,3]
# Output:
# [6,3,2]
# Explanation:
# B[0] = A[1] * A[2] = 6; B[1] = A[0] * A[2] = 3; B[2] = A[0] * A[1] = 2

class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        # write your code here
        f = [0 for _ in range(len(nums) + 1)]
        f[-1] = 1
        for i in range(len(nums) - 1, -1, -1):
            f[i] = f[i + 1] * nums[i]
        
        temp = 1
        result = []
        for i in range(len(nums)):
            result.append(temp * f[i + 1])
            temp *= nums[i]
        
        return result