class Solution:
    def sortSentence(self, s: str) -> str:
        word_list = s.split(' ')
        sentence_list = [""] * len(word_list)
        for word_pos in word_list:
            pos = int(word_pos[-1])-1
            word = word_pos[:-1]
            sentence_list[pos] = word 
        return " ".join(sentence_list)
