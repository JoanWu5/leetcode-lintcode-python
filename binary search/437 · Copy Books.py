# O(nlogrange)
from typing import (
    List,
)


class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """

    def copy_books(self, pages: List[int], k: int) -> int:
        # write your code here
        if not pages:
            return 0
        if k == 1:
            return sum(pages)
        if len(pages) <= k:
            return max(pages)

        left, right = max(pages), sum(pages)
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.getCopyMinutes(pages, mid) > k:
                left = mid
            else:
                right = mid

        if self.getCopyMinutes(pages, left) <= k:
            return left
        return right

    def getCopyMinutes(self, pages: List[int], speed: int) -> int:
        person = 0
        copy_page = 0
        for page in pages:
            if copy_page + page > speed:
                person += 1
                copy_page = page
            else:
                copy_page += page

        if copy_page > 0:
            person += 1
        return person
