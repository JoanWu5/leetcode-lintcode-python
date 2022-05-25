# O(n)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        left, right = self.findDifference(s, 0, len(s) - 1)
        if left >= right:
            return True
        
        return self.isPalindrome(s, left, right - 1) or self.isPalindrome(s, left + 1, right)
            
    
    def isPalindrome(self, s: str, left: int, right: int) -> bool:
        left, right = self.findDifference(s, left, right)
        return left >= right
            
    
    def findDifference(self, s: str, left, right):
        while left <= right:            
            if s[left] != s[right]:
                return left, right
            
            left += 1
            right -= 1
            
        return left, right