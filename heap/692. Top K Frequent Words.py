from heapq import heappush, heappop
from collections import Counter
from typing import List


class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word
        
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        frequency_map = Counter(words)
        frequency_heap = []
        
        for key, value in frequency_map.items():
            heappush(frequency_heap, Word(value, key))
            if len(frequency_heap) > k:
                heappop(frequency_heap)
        
        result = []
        while frequency_heap:
            result.append(heappop(frequency_heap).word)
        
        return result[::-1]
