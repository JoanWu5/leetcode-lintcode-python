# O(nlogLen), where Len is the longest length of the wood.
from typing import (
    List,
)


class Solution:
    """
    @param l: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def wood_cut(self, l: List[int], k: int) -> int:
        # write your code here
        if not l or sum(l) < k:
            return 0

        left, right = 1, min(max(l), sum(l) // k)

        while left + 1 < right:
            mid = left + (right - left) // 2
            pieces = self.get_wood_cut_pieces(l, mid)
            if pieces >= k:
                left = mid
            else:
                right = mid

        if self.get_wood_cut_pieces(l, right) >= k:
            return right
        return left

    def get_wood_cut_pieces(self, l: List[int], wood_length: int) -> int:
        count = 0
        for wood in l:
            count += wood // wood_length
        return count
