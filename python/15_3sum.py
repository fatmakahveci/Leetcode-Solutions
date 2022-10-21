class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        if len(nums) < 3:
            return []
    
        nums.sort()
        
        if nums[0] > 0 or nums[-1] < 0:
            return []

        res = []  
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            lo, hi = i+1, len(nums)-1
            target = -nums[i]
            while lo < hi:
                if nums[lo] + nums[hi] < target:
                    lo += 1
                elif nums[lo] + nums[hi] > target:
                    hi -= 1
                else:
                    res.append([ nums[lo], nums[i], nums[hi] ])
                    while lo < hi and nums[hi-1] == nums[hi]:
                        hi -= 1
                    while lo < hi and nums[lo] == nums[lo+1]:
                        lo += 1
                    lo += 1
                    hi -= 1
        
        return res
