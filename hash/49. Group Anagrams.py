from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for s in strs:
            sorted_str = tuple(sorted(s))
            anagram_map[sorted_str].append(s)
        
        return anagram_map.values()