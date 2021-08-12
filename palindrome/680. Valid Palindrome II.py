class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                deleteLeft = s[left + 1: right + 1]
                deleteRight = s[left: right]
                return deleteLeft == deleteLeft[:: -1] or deleteRight == deleteRight[:: -1]
            left += 1
            right -= 1
        
        return True