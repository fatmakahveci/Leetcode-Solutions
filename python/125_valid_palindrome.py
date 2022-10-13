class Solution:
    def isPalindrome(self, s: str) -> bool:

        alpha_s =''.join([c.lower() if (c.isalpha() or c.isdigit()) else '' for c in s])
        start, end = 0, len(alpha_s)-1
        while start <= end:
            if alpha_s[start] == alpha_s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True
