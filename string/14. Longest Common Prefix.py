from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
        
        result = strs[0]
        for i in range(1, len(strs)):
            length = min(len(result), len(strs[i]))
            k = 0
            while k < length:
                if result[k] == strs[i][k]:
                    k += 1
                else:
                    break
            result = result[:k]
        
        return "".join(result)
            