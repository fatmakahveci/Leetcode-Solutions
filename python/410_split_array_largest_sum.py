class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        '''
        3 1 2 4 5       m=3
        
        l=5 r=4 mid=5 res=5
        
        '''
        def can_split(largest): # 
            subarray = 0
            cur_sum = 0
            for n in nums: # 3 1 2 4 5
                cur_sum += n # 
                if cur_sum > largest:
                    subarray += 1 # 
                    cur_sum = n # 
            return subarray + 1 <= m 

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l+r)//2
            if can_split(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
