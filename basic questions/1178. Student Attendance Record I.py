# You are given a string representing an attendance record for a student. 
# The record only contains the following three characters:

# 'A' : Absent.
# 'L' : Late.
# 'P' : Present.
# A student could be rewarded if his attendance record 
# doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

# You need to return whether the student could be rewarded according to his attendance record.

# Example:
# Input: "PPALLP"
# Output: True


class Solution:
    """
    @param s: a string
    @return: whether the student could be rewarded according to his attendance record
    """
    def checkRecord(self, s):
        # Write your code here
        absent_record = 0
        late_record = 0
        for i in range(len(s)):
            if s[i] == 'A':
                absent_record += 1
            
            if i <= len(s) - 3 and s[i:i+3] == 'LLL':
                late_record += 1
        
        if absent_record > 1 or late_record >= 1:
            return False
        
        return True
