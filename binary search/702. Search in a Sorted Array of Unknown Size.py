from typing import List


class ArrayReader:
    def __init__(self) -> None:
        self.reader = []

    def get(self, index):
        return self.reader[index]

class Solution:
    def searchUnknownSizeArray(self, reader: ArrayReader, nums: List[int], target: int) -> int:
        array_length = 1
        while reader.get(nums[array_length]) < target:
            array_length *= 2
        
        left, right = array_length //2 , array_length
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
