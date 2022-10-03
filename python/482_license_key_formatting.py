class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-','').upper()
        n = len(s)
        if n < k:
            return s
        for i in range(n-k, n%k, -k):
            s = s[:i] + '-' + s[i:]
        if n%k != 0:
            s = s[:n%k]+'-'+s[n%k:]
        return s
