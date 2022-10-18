class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        # base conditions
        if not p or len(p) == 0 or not s or len(s) == 0:
            return
        
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]

        # independent of the previous case
        dp[0][0] = True

        # empty case
        for j in range(2,len(p)+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for j in range(1,len(p)+1):
            for i in range(1,len(s)+1):
                
                # single match
                if p[j-1] == s[i-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]

                # star match
                elif p[j-1] == '*':
                    if dp[i][j-2] or (s[i-1] == p[j-2] or p[j-2] == '.') and dp[i-1][j]:
                        dp[i][j] = True

        return dp[-1][-1]
