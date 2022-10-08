class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        def comb(i, k, subset):
            if k == len(subset):
                results.append(subset.copy())
                return
            for s in range(i, n):
                subset.append(nums[s])
                comb(s+1, k, subset)
                subset.pop()
        
        results = []
        n = len(nums)
        for k in range(n+1):
            comb(0, k, [])
        return results
