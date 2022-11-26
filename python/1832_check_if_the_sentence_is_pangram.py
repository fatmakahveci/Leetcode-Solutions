class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letter_dict = {}
        for i in range(26):
            letter_dict[chr(ord('a')+i)] = 0
        
        for letter in sentence:
            letter_dict[letter] += 1
        
        for i in range(26):
            if letter_dict[chr(ord('a')+i)] == 0:
                return False
        return True
        
