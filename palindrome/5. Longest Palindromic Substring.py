# O(n^2)
# two pointers
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        result = (0, 0)
        for i in range(len(s)):
            result = max(result, self.getPalindrome(s, i, i))
            result = max(result, self.getPalindrome(s, i, i + 1))
        
        return s[result[1]: result[0] + result[1]]
    
    def getPalindrome(self, s, left, right):
        while left >= 0 and right < len(s) and left <= right:
            if s[left] != s[right]:
                break
            left -= 1
            right += 1
        return right - left - 1, left + 1

# dp
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        n = len(s)
        isPalindorme = [[False] * n for _ in range(n)]
        for i in range(n):
            isPalindorme[i][i] = True
        
        start, longest = 0, 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                isPalindorme[i][i + 1] = True
                start = i
                longest = 2
        
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if isPalindorme[i + 1][j - 1] and s[i] == s[j]:
                    isPalindorme[i][j] = True
                
                if length > longest and isPalindorme[i][j]:
                    longest = length
                    start = i
        
        return s[start: start + longest]
        
        
                
                    
        