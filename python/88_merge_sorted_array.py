class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j = 0, 0
        while i < len(nums1) and j < n:
            if i == j + m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            elif nums1[i] <= nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                nums1[i+1:] = nums1[i:-1]
                nums1[i] = nums2[j]
                j += 1
                i += 1
