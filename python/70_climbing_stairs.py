class Solution:
    
    def climbStairs(self, n: int) -> int:
        ## Bottom-up
        if n == 1:
            return 1
        
        dp = [ 0, 1, 2 ]
        for _ in range(3, n+1):
            dp.append(sum(dp[-2:]))

        return dp[n]
