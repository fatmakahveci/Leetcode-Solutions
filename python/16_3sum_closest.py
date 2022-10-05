class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        diff = float("inf")
        nums.sort()
        for i in range(len(nums)-2):
            lo = i+1
            hi = len(nums)-1
            while lo < hi:
                three_sum = nums[i] + nums[lo] + nums[hi]
                if abs(target-three_sum) < abs(diff):
                    diff = target - three_sum
                if three_sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break    
        return target - diff
            
