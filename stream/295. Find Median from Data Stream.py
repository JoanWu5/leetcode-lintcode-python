from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_number_heap = []
        self.max_number_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_number_heap) == len(self.max_number_heap):
            heappush(self.min_number_heap, -heappushpop(self.max_number_heap, num))
        else:
            heappush(self.max_number_heap, -heappushpop(self.min_number_heap, -num))
        

    def findMedian(self) -> float:
        if len(self.min_number_heap) == len(self.max_number_heap):
            return (-self.min_number_heap[0] + self.max_number_heap[0]) / 2
        else:
            return -self.min_number_heap[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()