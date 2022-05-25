# O(n)
class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        
        letters = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left <= right and not self.isVowel(letters[left]):
                left += 1
            
            while left < right and not self.isVowel(letters[right]):
                right -= 1
            
            if left < right:
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right -= 1
        
        return "".join(letters)
    
    def isVowel(self, letter):
        return letter in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}