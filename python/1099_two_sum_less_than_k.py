class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        '''
        34 23 1  24 75 33 54 8  k = 60
        
        1  8  23 24 33 34 54 75
        lo                   hi
        '''
        res = -1
        
        nums.sort()
        
        lo, hi = 0, len(nums)-1
        while lo < hi:
            max_sum = nums[lo] + nums[hi]
            
            if max_sum >= k:
                hi -= 1
            else:
                res = max(res, max_sum)
                lo += 1
            
        return res
