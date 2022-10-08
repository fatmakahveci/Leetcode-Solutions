class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
#         dp = [ [1] * n for _ in range(m)]

#         for r in range(m-2,-1,-1):
#             for c in range(n-2,-1,-1):
#                 dp[r][c] = dp[r][c+1] + dp[r+1][c]

#         return dp[0][0]
        
        return math.factorial(m+n-2) // math.factorial(n-1) // math.factorial(m-1)
