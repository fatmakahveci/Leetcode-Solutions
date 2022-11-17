class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if int(str(n)[-1]) % 2 == 0:
            return n
        return n*2
