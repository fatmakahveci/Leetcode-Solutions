class Solution:
    def helper(self, x: float, n: int) -> float:
        if n == 0:
            return 1.0
        half = self.helper(x, n//2)
        if n % 2 == 0:
            return half * half
        return half * half * x

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            return self.helper(1/x, -n)
        return self.helper(x, n)
