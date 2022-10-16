class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = cur_min = 1

        for cur in nums:
            if cur == 0:
                cur_max, cur_min = 1, 1
                continue
            tmp_max = cur_max*cur
            cur_max = max(cur, tmp_max, cur_min*cur)
            cur_min = min(cur, tmp_max, cur_min*cur)
            res = max(res, cur_max)

        return res
