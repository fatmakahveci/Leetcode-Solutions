class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        for r in range(1, len(arr)+1, 2):
            for l in range(len(arr)-r+1):
                res += sum(arr[l:l+r])
        return res
