# For a given source string and a target string, you should output the first index(from 0) of target string in the source string.
# If the target does not exist in source, just return -1.

# Do I need to implement KMP Algorithm in a real interview?
# Not necessary. When you meet this problem in a real interview, 
# the interviewer may just want to test your basic implementation ability. 
# But make sure you confirm how to implement with the interviewer first.
# Example:
# Input:
# source = "source"
# target = "target"
# Output:
# -1


class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        target_length = len(target)
        for i in range(len(source) - target_length + 1):
            if source[i:i+target_length] == target:
                return i
        
        return -1
