# Given a year and month, return the days of that month.
# Example:
# Input: 
# 2020 
# 2
# Output: 
# 29

class Solution:
    """
    @param year: a number year
    @param month: a number month
    @return: Given the year and the month, return the number of days of the month.
    """
    def getTheMonthDays(self, year, month):
        # write your code here
        monthdays = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 
        9: 30, 10: 31, 11: 30, 12: 31}
        if month == 2:
            if self.isLeapYear(year):
                return 29
        
        return monthdays[month]

    def isLeapYear(self, year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
