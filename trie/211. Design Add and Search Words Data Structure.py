from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end = False
        
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for letter in word:
            current = current.children[letter]
        current.is_end = True

    def search(self, word: str) -> bool:
        def search_node(word, node):
            for index, letter in enumerate(word):
                if letter in node.children:
                    node = node.children[letter]
                else:
                    if letter == '.':
                        for child in node.children.keys():
                            if search_node(word[index + 1:], node.children[child]):
                                return True
                    return False
            return node.is_end
        
        return search_node(word, self.root)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)