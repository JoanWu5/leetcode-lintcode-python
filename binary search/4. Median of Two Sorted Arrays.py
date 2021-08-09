from typing import List


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
        
