class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        def range_(lower: int, upper: int) -> str:
            if lower == upper:
                return str(lower)
            return str(lower)+"->"+str(upper)
        
        if len(nums) == 0:
            return [range_(lower, upper)]

        interval_list = []
        prev = lower - 1
        for curr in nums:
            if prev + 1 <= curr - 1:
                interval_list.append(range_(prev+1,curr-1))
            prev = curr
        if nums[-1] < upper:
            interval_list.append(range_(nums[-1]+1,upper))
        return interval_list
