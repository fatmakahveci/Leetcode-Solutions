class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        l, r = 2, x//2
        while l <= r:
            mid = l + (r-l)//2
            if x < mid * mid:
                r = mid - 1
            elif mid * mid < x:
                l = mid + 1
            else:
                return mid
        return r
