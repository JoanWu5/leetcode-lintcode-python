from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates:
            return []
        
        result = []
        def recur(index, path, target):
            if target < 0:
                return
            
            if target == 0:
                result.append(list(path))
                return
            
            for i in range(index, len(candidates)):
                candidate = candidates[i]
                path.append(candidate)
                recur(i, path, target - candidate)
                path.pop()
            
        recur(0, [], target)
        return result