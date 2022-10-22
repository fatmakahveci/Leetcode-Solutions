class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[int(len(nums)/2)]
