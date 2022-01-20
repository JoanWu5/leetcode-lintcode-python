from typing import List
from collections import defaultdict


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = defaultdict(int)
        
        for i, char in enumerate(order):
            order_map[char] = i

        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]

            for index in range(len(current_word)):
                if index >= len(next_word):
                    return False
                
                if order_map[current_word[index]] > order_map[next_word[index]]:
                    return False
                elif order_map[current_word[index]] < order_map[next_word[index]]:
                    break

        
        return True
                    
                
            