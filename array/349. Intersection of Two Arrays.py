from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        
        result = []
        for num in set1:
            if num in set2:
                result.append(num)
        
        return result

# This is a Facebook interview question.
# They ask for the intersection, which has a trivial solution using a hash or a set.

# Then they ask you to solve it under these constraints:
# O(n) time and O(1) space (the resulting array of intersections is not taken into consideration).
# You are told the lists are sorted.

# Cases to take into consideration include:
# duplicates, negative values, single value lists, 0's, and empty list arguments.
# Other considerations might include
# sparse arrays.


class Solution2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        result = []
        pointer1, pointer2 = 0, 0
        while pointer1 < m and pointer2 < n:
            if nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
            elif nums1[pointer1] > nums2[pointer2]:
                pointer2 += 1
            else:
                if not result and result[-1] != nums1[pointer1]:
                    result.append(nums1[pointer1])
                pointer1 += 1
                pointer2 += 1
        return result