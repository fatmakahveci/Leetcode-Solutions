class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        res = 0
        for i in range(1, len(nums)-1):
            if (nums[i] - diff) in nums and (nums[i] + diff) in nums:
               res += 1
        return res
