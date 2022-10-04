class Solution:
    def myAtoi(self, s: str) -> int:
        i, n = 0, len(s)
        res = 0
        negative = 1

        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and s[i] == '-':
            i += 1
            negative = -1
        elif i < n and s[i] == '+':
            i += 1
            negative = 1
        
        while i < n and '0' <= s[i] <= '9':
            res = res * 10 + int(s[i])
            i += 1

        res *= negative
        if res < 0:
            return max(res, -2**31)
        return min(res, 2**31-1)
