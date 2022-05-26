from typing import List
from collections import defaultdict

# O(n^2)
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        num_dict1 = defaultdict(int)
        result = 0
        
        for num1 in nums1:
            for num2 in nums2:
                num_dict1[num1 + num2] += 1
        
        for num3 in nums3:
            for num4 in nums4:
                result += num_dict1[-num3 - num4]
        
        return result
                
                
# ksum Count: O(n^(k/2)) not understand
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        m = defaultdict(int)
        lists = [A, B, C, D]

        def nSumCount() -> int:
            addToHash(0, 0)
            return countComplements(len(lists) // 2, 0)

        def addToHash(i: int, total: int) -> None:
            if i == len(lists) // 2:
                m[total] = m[total] + 1
            else:
                for a in lists[i]:
                    addToHash(i + 1, total + a)

        def countComplements(i: int, complement: int) -> int:
            if i == len(lists):
                return m[complement]
            cnt = 0
            for a in lists[i]:
                cnt += countComplements(i + 1, complement - a)
            return cnt

        return nSumCount()