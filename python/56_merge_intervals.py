class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if 0 <= len(intervals) <= 1:
            return intervals
        intervals.sort(key=lambda x:x[0])
        interval_list = [intervals[0]]
        for interval in intervals[1:]:
            if interval_list[-1][1] < interval[0]:
                interval_list.append(interval)
            else:
                interval_list[-1][1] = max(interval_list[-1][1], interval[1])
        return interval_list
