class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        twice = nums[0]
        for num in nums[1:]:
            twice ^= num
        return twice
