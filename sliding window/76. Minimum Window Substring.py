# O(N)
from collections import Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        t_char_frequency = Counter(t)
        s_char_frequency = dict()
        start = 0
        min_length = math.inf
        min_start = 0
        length = 0
        
        for end in range(len(s)):
            character = s[end]
            s_char_frequency[character] = s_char_frequency.get(character, 0) + 1
            if character in t_char_frequency and s_char_frequency[character] == t_char_frequency[character]:
                length += 1
            
            while start <= end and length == len(t_char_frequency):
                left_character = s[start]
                if end - start + 1 < min_length:
                    min_length = end - start + 1
                    min_start = start
                s_char_frequency[left_character] -= 1
                if left_character in t_char_frequency and s_char_frequency[left_character] < t_char_frequency[left_character]:
                    length -= 1
                start += 1
        return "" if min_length == math.inf else s[min_start: min_start + min_length]
                
            