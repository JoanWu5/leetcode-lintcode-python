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
        
        
                
                    
        