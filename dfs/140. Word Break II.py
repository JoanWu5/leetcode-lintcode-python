from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not wordDict:
            return []
        
        result = []
        self.dfs(s, wordDict, [], result, 0)
        return result
    
    def dfs(self, s, wordDict, path, result, index):
        if index == len(s):
            if ''.join(path) == s:
                result.append(' '.join(path))
            return
        
        for word in wordDict:
            word_length = len(word)
            if s[index: index + word_length] == word:
                self.dfs(s, wordDict, path + [word], result, index + word_length)
        
                
        
        