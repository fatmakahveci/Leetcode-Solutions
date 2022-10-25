class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(i):
            if i < 2:
                return max(nums[:i+1])
            if i not in hash_map:
                hash_map[i] = max(dp(i-1), dp(i-2) + nums[i])
            return hash_map[i]
        hash_map = {}
        return dp(len(nums)-1)
