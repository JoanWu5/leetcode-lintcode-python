# O(logn)
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 1, x
        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid
            else:
                left = mid
        if right * right <= x:
            return right
        return left
