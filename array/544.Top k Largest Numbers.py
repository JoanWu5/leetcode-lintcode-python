from typing import (
    List,
)
import random

# O(nlogk)
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums: List[int], k: int) -> List[int]:
        # write your code here
        if not nums or k <= 0:
            return []

        self.select(nums, 0, len(nums) - 1, k - 1)
        return nums[:k]

    
    def partition(self, nums: List[int], left: int, right: int) -> int:
        pivot_index = random.randint(left, right)
        pivot = nums[pivot_index]
        nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
        
        pointer = left
        for i in range(left, right):
            if nums[i] >= pivot:
                nums[pointer], nums[i] = nums[i], nums[pointer]
                pointer += 1
        nums[pointer], nums[right] = nums[right], nums[pointer]
        return pointer
    
    def select(self, nums: List[int], left: int, right: int, k: int):
        if left >= right:
            return

        split = self.partition(nums, left, right)
        if split == k:
            self.select(nums, left, split - 1, k - 1)
            return
        
        if split > k:
            self.select(nums, left, split - 1, k)
            return
        
        self.select(nums, left, split - 1, k)
        self.select(nums, split + 1, right, k)