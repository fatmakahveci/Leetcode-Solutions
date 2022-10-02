class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_sentence = False
        self.hot = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, sentence, hot):
        node = self.root
        for char in sentence:
            if not char in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_sentence = True
        node.hot -= hot
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.build_trie(sentences, times)
        self.reset_search()

    def build_trie(self, sentences, times):
        self.trie = Trie()
        for i, sentence in enumerate(sentences):
            self.trie.insert(sentence, times[i])
    
    def reset_search(self):
        self.search_term = ""
        self.last_node = self.trie.root
        self.no_match = False
        
    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.search_term, 1)
            self.reset_search()
        else:
            self.search_term += c

            if not c in self.last_node.children or self.no_match:
                self.no_match = True
                return []
            
            self.last_node = self.last_node.children[c]
            result = []
            self.dfs(self.last_node, self.search_term, result)

            return [sentences[1] for sentences in sorted(result)[:3]]

    def dfs(self, node, path, result):
        if node.is_sentence:
            result.append((node.hot, path))
        
        for char in node.children:
            self.dfs(node.children[char], path+char, result)
