from collections import deque, defaultdict
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList or beginWord == endWord:
            return 0
        
        neighbors = defaultdict(list)
        wordLength = len(beginWord)
        
        for word in wordList:
            for i in range(wordLength):
                neighbors[word[:i] + "*" + word[i + 1:]].append(word)
            
        wordCount = dict()
        
        queue = deque([(beginWord, 1)])
        wordCount[beginWord] = 1
        
        while queue:
            word, length = queue.popleft()
            for i in range(wordLength):
                wordStar = word[:i] + "*" + word[i + 1:]
                for anotherWord in neighbors[wordStar]:
                    if anotherWord not in wordCount or wordCount[anotherWord] > length + 1:
                        wordCount[anotherWord] = length + 1
                        queue.append((anotherWord, length + 1))
        
        return wordCount[endWord] if endWord in wordCount else 0
        
        