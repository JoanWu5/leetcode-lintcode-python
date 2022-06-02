# O(n + m)
from collections import Counter
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        frequencyMap1 = Counter(nums1)
        frequencyMap2 = Counter(nums2)
        
        result = []
        for num, frequency in frequencyMap1.items():
            if num in frequencyMap2:
                result.extend([num] * min(frequency, frequencyMap2[num]))
        return result
            