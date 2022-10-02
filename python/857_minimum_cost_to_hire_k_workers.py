class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        '''
        qual: 10 20  5
        wage: 70 50  30
        rate: 7  2.5 6
        
        workers = (2.5, 20, 50) (6, 5, 30) (7, 10, 70)
        
        heap =
          -20
        sum_q = 20
          
        heap     =
            -20
        -5       
        sum_q    = 25
        min_cost = 150
        
        heap =
            -20
        -5     -10
        sum_q = 15
        min_cost = 15 * 7 = 105
        '''
        
        workers = sorted( ( (float(w)/q, q, w) for q, w in zip(quality, wage) ), key=lambda x:x[0] )
        min_cost = float('inf')
        pool = []
        sum_q = 0
        for rate, q, w in workers:

            heapq.heappush(pool, -q)
            sum_q += q

            if len(pool) > k:
                sum_q += heapq.heappop(pool)

            if len(pool) == k:
                min_cost = min(min_cost, rate*sum_q)

        return float(min_cost)
