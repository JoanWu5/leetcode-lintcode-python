from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phoneMap = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'], 
                   5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 7: ['p', 'q', 'r', 's'],
                   8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}
        
        result = []
        self.dfs(0, [], result, digits, phoneMap)
        return result
    
    def dfs(self, index, path, result, digits, phoneMap):
        if len(path) == len(digits):
            result.append(''.join(list(path)))
            return
        
        for i in range(index, len(digits)):
            possibleLetter = phoneMap[int(digits[i])]
            for letter in possibleLetter:
                path.append(letter)
                self.dfs(i + 1, path, result, digits, phoneMap)
                path.pop()