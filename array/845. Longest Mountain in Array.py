# O(n)
from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        if not arr:
            return 0

        n = len(arr)
        result, base = 0, 0
        while base < n:
            left = base
            if left + 1 < n and arr[left] < arr[left + 1]:
                while left + 1 < n and arr[left] < arr[left + 1]:
                    left += 1

                if left + 1 < n and arr[left] > arr[left + 1]:
                    while left + 1 < n and arr[left] > arr[left + 1]:
                        left += 1
                    result = max(result, left - base + 1)
            base = max(base + 1, left)

        return result
