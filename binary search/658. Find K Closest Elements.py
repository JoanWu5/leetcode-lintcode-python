# O(logn + klogk)
from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        if len(arr) <= k:
            return arr
        
        right = self.binarySearch(arr, x)
        left = right - 1
        result = []
        for i in range(k):
            if self.isLeftClose(arr, x, left, right):
                result.append(arr[left])
                left -= 1
            else:
                result.append(arr[right])
                right += 1
        return sorted(result)
    
    def binarySearch(self, arr: List[int], x: int) -> int:
        left, right = 0, len(arr) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if arr[mid] == x:
                return mid
            if arr[mid] > x:
                right = mid
            else:
                left = mid
        return right
    
    def isLeftClose(self, arr: List[int], x: int, left: int, right: int) -> bool:
        if left < 0:
            return False
        if right >= len(arr):
            return True
        
        if abs(arr[left] - x) <= abs(arr[right] - x):
            return True
        return False

# O(log(n-k) + k)
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if not arr:
            return []
        if len(arr) <= k:
            return arr
        
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + (right - left) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left: left + k]