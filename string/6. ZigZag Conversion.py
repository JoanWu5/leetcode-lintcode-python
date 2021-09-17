class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s or numRows == 0:
            return ""
        
        if numRows == 1:
            return s
        
        result = [""] * len(s)
        mod = 2 * numRows - 2
        
        for i in range(len(s)):
            position = i % mod
            if position >= numRows:
                position = mod - position
            result[position] += s[i]

        return "".join(result)
        