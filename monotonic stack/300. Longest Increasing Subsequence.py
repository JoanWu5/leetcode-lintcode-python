from typing import List
import bisect


# dp: O(N^2) space: O(N)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

# stack Improve With Binary Search O(NlogN), space: O(N)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            else:
                # partition array, the left is <= array[index], right >= array[index]
                i = bisect.bisect_left(sub, num)
                sub[i] = num
        return len(sub)
