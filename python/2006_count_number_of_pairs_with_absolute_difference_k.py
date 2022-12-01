class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        
        from collections import Counter

        res = 0
        num_counter = Counter(nums)
        for num in num_counter.keys():
            if (num + k) in num_counter:
                res += num_counter[num] * num_counter[num + k]
        return res
