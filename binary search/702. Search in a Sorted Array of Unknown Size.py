# O(logn)
class ArrayReader:
    def __init__(self) -> None:
        self.reader = []

    def get(self, index):
        return self.reader[index]

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 0
        right = 1
        while reader.get(right) < target:
            right *= 2
        
        while left + 1 < right:
            mid = left + (right - left) // 2
            if reader.get(mid) == target:
                return mid
            if reader.get(mid) > target:
                right = mid
            else:
                left = mid
        
        if reader.get(left) == target:
            return left
        if reader.get(right) == target:
            return right
        
        return -1
