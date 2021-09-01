class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        presum_dict = {0: - 1}
        max_length = 0
        presum = 0

        for i in range(len(nums)):
            presum += nums[i]
            if presum - k in presum_dict:
                max_length = max(max_length, i - presum_dict[presum - k])
            
            if presum not in presum_dict:
                presum_dict[presum] = i
        
        return max_length