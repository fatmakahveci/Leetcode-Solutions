class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        checker = set(nums1)
        for i in nums2:
            if i in checker:
                ret.append(i)
                checker.remove(i)
        return ret
