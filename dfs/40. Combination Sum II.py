from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        result = []
        candidates.sort()
        
        def recur(index, path, target):            
            if target == 0:
                result.append(list(path))
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                candidate = candidates[i]
                if target < candidate:
                    break
                path.append(candidate)
                recur(i + 1, path, target - candidate)
                path.pop()
        
        recur(0, [], target)
        return result