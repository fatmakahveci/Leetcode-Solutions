class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            if nums[i] >= end - i:
                end = i
        return end == 0
