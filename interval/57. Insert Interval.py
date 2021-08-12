from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not newInterval:
            return intervals
        
        result = []
        overlapInterval = newInterval
        for i, interval in enumerate(intervals):
            if interval[1] < overlapInterval[0]:
                result.append(interval)
            elif interval[0] > overlapInterval[1]:
                result.append(overlapInterval)
                return result + intervals[i:]
            else:
                overlapInterval[0] = min(interval[0], overlapInterval[0])
                overlapInterval[1] = max(interval[1], overlapInterval[1])
        
        result.append(overlapInterval)
        return result
            