# Given an array of integers, the majority number is the number that occurs more than half of the size of the array. Find it.

# You may assume that the array is non-empty and the majority number always exist in the array.

# Example:
# Input:
# array = [1, 1, 1, 1, 2, 2, 2]
# Output:
# 1

class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        count = 0
        majority_num = None
        for num in nums:
            if majority_num is None:
                count, majority_num = 1, num
            else:
                if num == majority_num:
                    count += 1
                else:
                    count -= 1
            
                if count == 0:
                    majority_num = None

        return majority_num
