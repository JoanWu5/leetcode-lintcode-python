# Find the second max number in a given array.

# You can assume the array contains at least two numbers.
# The second max number is the second number in a descending array.

# Example:
# Input: [1,3,2,4]
# Output: 3
import math

class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        # write your code here
        current_index, current_max = None, -math.inf
        previous_index, previous_max = None, math.inf

        for _ in range(2):
            for j in range(len(nums)):
                if nums[j] > current_max and nums[j] < previous_max:
                    current_max = nums[j]
                    current_index = j
                elif nums[j] == previous_max and j > previous_index:
                    current_max = nums[j]
                    current_index = j
                    break

            previous_max = current_max
            previous_index = current_index
            current_max = -math.inf
        
        return previous_max