class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for l in range(1, len(arr)+1, 2):
            for r in range(len(arr)-l+1):
                res += sum(arr[r:l+r])
        return res
