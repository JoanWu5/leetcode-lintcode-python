"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        # write your code here
        if not airplanes:
            return 0
        
        points = []
        for airplane in airplanes:
            points.append([airplane.start, 1])
            points.append([airplane.end, -1])
        
        numberAirplanes, maxNumAirplanes = 0, 0
        for _, count in sorted(points):
            numberAirplanes += count
            maxNumAirplanes = max(maxNumAirplanes, numberAirplanes)
        
        return maxNumAirplanes
