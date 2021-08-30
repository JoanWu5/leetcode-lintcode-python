# O(N)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not str:
            return 0
        
        char_dict = dict()
        max_length = 0
        start = 0
        
        for i in range(len(s)):
            character = s[i]
            if character in char_dict and start <= char_dict[character]:
                start = char_dict[character] + 1
            else:
                max_length = max(max_length, i - start + 1)
        
            char_dict[character] = i
            
        return max_length

s = Solution()              
print(s.lengthOfLongestSubstring("abcabcbb"))               