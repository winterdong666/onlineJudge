# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        def getStart(ele):
            return ele.start
        
        intervals.sort(key = getStart)
        
        res = []
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1
        if i == len(intervals):
            res.append(newInterval)
            return res
        tmp = newInterval
        if intervals[i].start <= newInterval.end:
            tmp.start = min(intervals[i].start, newInterval.start)
            tmp.end = max(intervals[i].end, newInterval.end)
            i += 1
            while i < len(intervals) and intervals[i].start <= newInterval.end:
                tmp.end = max(intervals[i].end, newInterval.end)
                i += 1
        res.append(tmp)
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res
