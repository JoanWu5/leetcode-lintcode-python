# Determine whether year n is a leap year.return true if n is a leap year.

# A leap year (also known as an intercalary year or bissextile year) is a calendar year containing one additional day.
# if a year is divisible by 4 and not divisible by 100 or divisible by 400,it is a leap year. --wikipedia

# Example:

# Input : n = 2008
# Output : true

class Solution:
    """
    @param n: a number represent year
    @return: whether year n is a leap year.
    """
    def isLeapYear(self, n):
        # write your code here
        return n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)