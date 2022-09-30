class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:
        if end_word not in word_list:
            return 0

        def build_graph():

            from collections import defaultdict

            pattern_dict = defaultdict(list)
            word_list.append(begin_word)
            for word in word_list:
                for i in range(len(word)):
                    pattern_dict[word[:i]+'*'+word[i+1:]].append(word)

            return pattern_dict

        def bfs():
            visited = [begin_word]
            q = [(begin_word, 1)]
            while q:
                word, level = q.pop(0)
                for i in range(len(begin_word)):
                    subpattern = word[:i]+'*'+word[i+1:]
                    for pattern in pattern_dict[subpattern]:
                        if pattern == end_word:
                            return level+1
                        if pattern not in visited:
                            visited.append(pattern)
                            q.append((pattern, level+1))
                pattern_dict[subpattern] = []
            return 0

        pattern_dict = build_graph()

        return bfs()
