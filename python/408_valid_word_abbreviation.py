class Solution:
    
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w_i, a_i = 0, 0
        
        while w_i < len(word) and a_i < len(abbr):
            skip_a_i = 0
            if abbr[a_i] == word[w_i]:
                a_i += 1
                w_i += 1

            elif abbr[a_i] == "0":
                return False

            elif abbr[a_i].isnumeric():
                while a_i < len(abbr) and abbr[a_i].isnumeric():
                    skip_a_i = int(abbr[a_i]) + skip_a_i * 10
                    a_i += 1
                w_i += int(skip_a_i)
            else:
                return False

        return a_i == len(abbr) and w_i == len(word)
