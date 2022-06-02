# O(n^2)
from typing import List


class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(k):
            for i in range(k // 2):
                arr[i], arr[k - 1 - i] = arr[k - 1 - i], arr[i]

        result = []
        sort_nums = len(arr)

        while sort_nums > 0:
            index = arr.index(sort_nums)
            if index != len(arr) - 1:
                if index != 0:
                    result.append(index + 1)
                    flip(index + 1)
                result.append(sort_nums)
                flip(sort_nums)

            sort_nums -= 1

        return result
