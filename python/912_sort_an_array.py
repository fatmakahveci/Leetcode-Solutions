class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums) # Timsort = Merge + Insertion # Best: O(n) # Worst: O(nlogn)
