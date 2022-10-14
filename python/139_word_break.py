class Solution:
    def wordBreak(self, s, wordDict):
        dp = [True] + [ False for i in range(len(s)) ]
        
        for end in range(1, len(s)+1):
            for word in wordDict:
                if dp[end-len(word)] and s[end-len(word):end] == word:
                    dp[end] = True
        return dp[-1]
