class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        for i in range(nums.count(val)):
                nums.remove(val)
                n -= 1
        return n
