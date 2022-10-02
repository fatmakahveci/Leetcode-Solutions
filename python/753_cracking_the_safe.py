class Solution(object):
    def crackSafe(self, n, k):
        ans = "0" * (n - 1)
        visits = set()
        for _ in range(k ** n):
            if n > 1:
                current = ans[-n+1:]
            else:
                current = ''
            for y in range(k - 1, -1, -1):
                if current + str(y) not in visits:
                    visits.add(current + str(y))
                    ans += str(y)
                    break
        return ans
