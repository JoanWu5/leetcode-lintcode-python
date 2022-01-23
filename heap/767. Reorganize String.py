from heapq import heappush, heappop
from collections import Counter


class Solution:
    def reorganizeString(self, s: str) -> str:
        frequency_map = Counter(s)
        frequency_heap = []
        
        for char, freq in frequency_map.items():
            heappush(frequency_heap, (-freq, char))
        
        result = ''
        while frequency_heap:
            freq, char = heappop(frequency_heap)
            if not result or result[-1] != char:
                if freq + 1 < 0:
                    heappush(frequency_heap, (freq + 1, char))
                result += char
            else:
                if frequency_heap:
                    freq2, char2 = heappop(frequency_heap)
                    if freq2 + 1 < 0:
                        heappush(frequency_heap, (freq2 + 1, char2))

                    heappush(frequency_heap, (freq, char))
                    result += char2
        
        return result if len(result) == len(s) else ''
        