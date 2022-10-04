class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        a b c a b c b b
        f     l
        
        max_len = 4
        first = 0
        last_seen = {a:3, b:2, c:3}
        '''
        max_len = 0
        first = 0
        last_seen = {}
        
        for last,ch in enumerate(s):
            if ch in last_seen:
                first = max(first, last_seen[ch])
            max_len = max(max_len,last-first+1)
            last_seen[ch] = last+1
        return max_len
