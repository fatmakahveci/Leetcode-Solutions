class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "": return ""
        
        from collections import Counter
        
        count_t = Counter(t)
        window = {}
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("inf")
        l = 0
        for r, c in enumerate(s):
            window[c] = 1 + window.get(c, 0)
            
            if c in count_t and window[c] == count_t[c]:
                have += 1
        
            while have == need:
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""
