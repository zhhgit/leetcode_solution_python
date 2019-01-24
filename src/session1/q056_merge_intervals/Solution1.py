# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution1:
    def merge(self, intervals):
        if len(intervals) == 0 or len(intervals) == 1:
            return intervals
        intervals.sort(key=self.sortMethod)
        prev = None
        ret = []
        for i in range(0,len(intervals)):
            if prev is None and i == 0:
                prev = intervals[i]
            else:
                curr = intervals[i]
                # 包含
                if curr.end <= prev.end:
                    continue
                # 分离
                elif prev.end < curr.start:
                    ret.append(prev)
                    prev = curr
                # 相交
                else:
                    prev = Interval(prev.start,curr.end)
        ret.append(prev)
        return ret

    def sortMethod(self,interval):
        return interval.start

    def printIntervals(self,intervals):
        for i in range(0,len(intervals)):
            interval = intervals[i]
            print("[" + str(interval.start) + "," + str(interval.end) + "]")

arr = [[15,18],[1,3],[2,6],[8,10]]
s = Solution1()
intervals = []
for i in range(0,len(arr)):
    interval = Interval(arr[i][0],arr[i][1])
    intervals.append(interval)
result = s.merge(intervals)
s.printIntervals(result)
