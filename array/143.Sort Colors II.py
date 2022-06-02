# O(nk)
from typing import (
    List,
)

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        # write your code here
        if not colors or k == 1:
            return
        
        left, right = 0, len(colors) - 1
        for pivot in range(1, k // 2 + 1):
            left, right = self.partition(colors, left, right, pivot, k + 1 - pivot)
            if left >= right:
                return
        
    def partition(self, nums: List[int], left: int, right: int, pivot_left: int, pivot_right: int):
        current = left
        while current <= right:
            if nums[current] == pivot_left:
                nums[current], nums[left] = nums[left], nums[current]
                left += 1
                current += 1
            elif nums[current] == pivot_right:
                nums[current], nums[right] = nums[right], nums[current]
                right -= 1
            else:
                current += 1
            
        return left, right

# O(nlogk)
class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        # write your code here
        if not colors or k == 1:
            return
        
        self.partition(colors, 0, len(colors) - 1, 1, k)
        
    def partition(self, nums: List[int], index_from: int, index_to: int, pivot_left: int, pivot_right: int):
        if index_from >= index_to or pivot_left >= pivot_right:
            return

        color = (pivot_right + pivot_left) // 2
        left, right = index_from, index_to
        while left <= right:
            while left <= right and nums[left] <= color:
                left += 1
            while left <= right and nums[right] > color:
                right -= 1
            
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        self.partition(nums, index_from, left, pivot_left, color)
        self.partition(nums, right, index_to, color + 1, pivot_right)