# O(logn)
# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass


class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 0:
            return 0
        
        left, right = 1, n
        while left + 1 < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid
        
        if isBadVersion(left):
            return left
        if isBadVersion(right):
            return right
        return 0