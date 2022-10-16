class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        letter_map = {}
        left, right = 0, 0
        max_len = 0
        while right < len(s):
            letter_map[s[right]] = right
            if len(letter_map) == 3:
                lru_letter = min(letter_map, key=letter_map.get)
                left = letter_map[lru_letter]+1
                del letter_map[lru_letter]
            max_len = max(max_len, right-left+1)
            right += 1
    
        return max_len
