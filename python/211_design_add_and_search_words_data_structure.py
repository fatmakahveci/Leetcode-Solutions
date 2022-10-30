class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_trie = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.end_of_trie = True

    def search(self, word: str) -> bool:
        
        def dfs(word, curr):
            for i, char in enumerate(word):
                if char == ".":
                    for child in curr.children:
                        childNode = curr.children[child]
                        if dfs(word[i+1:], childNode):
                            return True
                    return False

                if char not in curr.children:
                    return False

                curr = curr.children[char]
            return curr.end_of_trie

        curr = self.root
        return dfs(word, curr)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
