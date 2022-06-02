# O(n)
from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        # write your code here
        if not a:
            return
        
        count_positive = 0
        for num in a:
            if num > 0:
                count_positive += 1

        count_negative = len(a) - count_positive
        if abs(count_positive - count_negative) > 1:
            return
            
        self.partition(a, 0, len(a) - 1, count_positive >= count_negative)
        print(a)
        self.interleaving(a, count_positive == count_negative)
    
    def partition(self, a: List[int], left: int, right: int, is_positive_more: bool):
        flag = 1 if is_positive_more else -1
        while left <= right:
            while left <= right and a[left] * flag > 0:
                left += 1
            while left <= right and a[right] * flag < 0:
                right -= 1
            
            if left <= right:
                a[left], a[right] = a[right], a[left]
                left += 1
                right -= 1
    
    def interleaving(self, a: List[int], has_same_length: bool):
        left, right = 1, len(a) - 1
        if has_same_length:
            right -= 1
        
        while left <= right:
            a[left], a[right] = a[right], a[left]
            left += 2
            right -= 2



        