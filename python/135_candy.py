class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        12 4 3 11 34 34 1 67
        1  1 1 2  3  1  1 2
        3  2 1 1  1  2  1 1
        
        3  2 1 2  3  2  1 2
        '''
        candies = [1] * len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        
        res = candies[-1]
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
            res += candies[i]
        return res
