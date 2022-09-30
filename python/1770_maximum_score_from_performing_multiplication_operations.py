class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        @lru_cache(2000)
        def dp(left, right, i):
            if i == len(multipliers):
                return 0
            return max( multipliers[i] * nums[left] + dp( left+1, right, i+1 ),
                        multipliers[i] * nums[right] + dp( left, right-1, i+1))
        return dp(0, len(nums)-1, 0)
