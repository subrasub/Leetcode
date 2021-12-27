class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float('-inf')
        res = 0

        for s, e in intervals:
            if s >= end:
                end = e
            else:
                res += 1

        return res