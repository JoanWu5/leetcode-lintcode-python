class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        
        result = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not self.isVowel(result[left]):
                left += 1
            while left < right and not self.isVowel(result[right]):
                right -= 1
            if left < right:
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1
        
        return ''.join(result)
    
    
    def isVowel(self, character: str) -> bool:
        vowels = list('aeiouAEIOU')
        if character in vowels:
            return True
        return False