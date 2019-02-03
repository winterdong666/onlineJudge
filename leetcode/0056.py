# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) <= 1:
            return intervals
        def takeFirst(ele):
            return ele.start
        intervals.sort(key = takeFirst)
        res = []
        tmp = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start > tmp.end:
                res.append(tmp)
                tmp = intervals[i]
            else:
                tmp.end = max(tmp.end, intervals[i].end)
        res.append(tmp)
        return res
