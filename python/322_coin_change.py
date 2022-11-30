class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")
            if amount not in memo:
                memo[amount] = min([1 + dp(amount - coin) for coin in coins])
            return memo[amount]
        
        minimum = dp(amount)
        return minimum if minimum != float("inf") else -1
