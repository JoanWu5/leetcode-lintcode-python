class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        
        romanMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        n = len(s)
        result = 0
        for i in range(1, n):
            if romanMap[s[i]] > romanMap[s[i - 1]]:
                result -= romanMap[s[i - 1]]
            else:
                result += romanMap[s[i - 1]]
        
        result += romanMap[s[-1]]
        return result