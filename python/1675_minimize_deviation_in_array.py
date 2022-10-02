class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        import heapq
        from sys import maxsize
        
        pq = [] # to update the current max
        min_num = maxsize
        
        for num in nums:
            if num % 2 == 0:
                heapq.heappush(pq, -num)
                min_num = min(min_num, num)
            else:
                heapq.heappush(pq, -num*2)
                min_num = min(min_num, num*2)

        ans = maxsize
        while pq:
            cur = -heapq.heappop(pq)
            ans = min(ans, cur-min_num)
            if cur % 2 == 1: break
            heapq.heappush(pq, -cur//2)
            min_num = min(min_num, cur//2)

        return ans
