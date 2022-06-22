# O(nlogm + mlogn)
from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image or not image[0]:
            return 0
        m = len(image)
        n = len(image[0])
        left = self.searchColumns(image, 0, y, True)
        right = self.searchColumns(image, y + 1, n, False)
        top = self.searchRows(image, 0, x, left, right, True)
        bottom = self.searchRows(image, x + 1, m, left, right, False)
        return (right - left) * (bottom - top)

    def searchColumns(self, image: List[List[str]], i: int, j: int, white_to_black: bool):
        m = len(image)
        while i < j:
            mid = (i + j) // 2
            if any(image[k][mid] == '1' for k in range(m)) == white_to_black:
                j = mid
            else:
                i = mid + 1
        return i

    def searchRows(self, image: List[List[str]], i: int, j: int, left: int, right: int, white_to_black: bool):
        while i < j:
            mid = (i + j) // 2
            if any(image[mid][k] == '1' for k in range(left, right)) == white_to_black:
                j = mid
            else:
                i = mid + 1
        return i
