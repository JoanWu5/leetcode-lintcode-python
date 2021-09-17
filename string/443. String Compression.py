from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        if not chars:
            return 0
        
        pointer, i = 0, 0
        count = 1
        while i < len(chars):
            chars[pointer] = chars[i]
            count = 1
            while i + 1 < len(chars) and chars[i] == chars[i + 1]:
                i += 1
                count += 1
            
            if count > 1:
                for c in str(count):
                    pointer += 1
                    chars[pointer] = c
            
            pointer += 1
            i += 1
        return pointer