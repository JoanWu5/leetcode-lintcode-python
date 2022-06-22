from typing import List

# O(log(n + m))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        totalLength = len(nums1) + len(nums2)
        if totalLength % 2 == 1:
            return self.findKth(nums1, 0, nums2, 0, totalLength // 2 + 1)
        else:
            return (self.findKth(nums1, 0, nums2, 0, totalLength // 2) + 
            self.findKth(nums1, 0, nums2, 0, totalLength // 2 + 1)) / 2
    
    def findKth(self, nums1, index_nums1, nums2, index_nums2, k):
        if len(nums1) == index_nums1:
            return nums2[index_nums2 + k - 1]
        if len(nums2) == index_nums2:
            return nums1[index_nums1 + k - 1]
        if k == 1:
            return min(nums1[index_nums1], nums2[index_nums2])
        
        a = nums1[index_nums1 + k // 2 - 1] if index_nums1 + k // 2 <= len(nums1) else None
        b = nums2[index_nums2 + k // 2 - 1] if index_nums2 + k // 2 <= len(nums2) else None
        if b is None or (a is not None and a < b):
            return self.findKth(nums1, index_nums1 + k // 2, nums2, index_nums2, k - k // 2)
        return self.findKth(nums1, index_nums1, nums2, index_nums2 + k // 2, k - k // 2)
    
# binary search 
# O(range * log(n + m))
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_length = len(nums1) + len(nums2)
        if total_length % 2 == 0:
            return (self.findKth(nums1, nums2, total_length // 2 - 1) + self.findKth(nums1, nums2, total_length // 2)) / 2
        return self.findKth(nums1, nums2, total_length // 2)
    
    def findKth(self, nums1: List[int], nums2: List[int], k:int):
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]
        
        left, right = min(nums1[0], nums2[0]), max(nums1[-1], nums2[-1])
        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.countSmallerOrEqual(nums1, mid) + self.countSmallerOrEqual(nums2, mid) >= k + 1:
                right = mid
            else:
                left = mid

        if self.countSmallerOrEqual(nums1, left) + self.countSmallerOrEqual(nums2, left) >= k + 1:
            return left
        return right
                
    
    def countSmallerOrEqual(self, arr: List[int], number: int):
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if arr[mid] > number:
                right = mid
            else:
                left = mid
        
        if arr[left] > number:
            return left
        if arr[right] > number:
            return right
        return len(arr)
