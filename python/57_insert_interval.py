class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        '''
        intervals:   12 3---5 67 8-10 11-16
        new_interval:             9----12
                          4------8
        
        '''
        res = []
        
        for i in range(len(intervals)):
            if intervals[i][1] < new_interval[0]:
                res.append(intervals[i])
            elif new_interval[1] < intervals[i][0]:
                res.append(new_interval)
                return res + intervals[i:]
            else:
                new_interval = [min(new_interval[0], intervals[i][0]), max(new_interval[1], intervals[i][1])]
        
        res.append(new_interval)
        
        return res

