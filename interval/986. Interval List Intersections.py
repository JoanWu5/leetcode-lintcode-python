from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if not firstList or not secondList:
            return []
        
        result = []
        firstPointer, secondPointer = 0, 0
        while firstPointer < len(firstList) and secondPointer < len(secondList):
            lo = max(firstList[firstPointer][0], secondList[secondPointer][0])
            hi = min(firstList[firstPointer][1], secondList[secondPointer][1])
            if lo <= hi:
                result.append([lo, hi])
            
            if firstList[firstPointer][1] < secondList[secondPointer][1]:
                firstPointer += 1
            else:
                secondPointer += 1
            
            
        return result