class TrieNode:
    def __init__(self):
        self.children = {}
        self.words = []
    
    def add_word(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            curr.words.append(word)
    
    def get_words(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]
        return curr.words
    
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        trie_root = TrieNode()
        for word in words:
            trie_root.add_word(word)

        def backtrack(curr_words, i):
            if i == n:
                ans.append(curr_words[:])
                return

            prefix = ''.join(word[i] for word in curr_words)
            
            words = trie_root.get_words(prefix)
            
            for word in words:
                curr_words.append(word)
                backtrack(curr_words, i+1)
                curr_words.pop()
        
        ans = []
        n = len(words[0])
        for word in words:
            backtrack([word], 1)

        return ans
