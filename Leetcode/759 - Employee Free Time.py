"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # flatten the input schedules
        temp = []
        for i in schedule:
            [temp.append(item) for item in i]

        # sort schedules by the start time
        temp.sort(key= lambda x: x.start)

        # merge the intervals
        merged = []
        for interval in temp:
            if not merged or interval.start > merged[-1].end:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        # find employee free times
        res = []
        for i in range(1, len(merged)):
            res.append(Interval(merged[i-1].end, merged[i].start))

        return res

