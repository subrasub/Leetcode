class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        start, end = newInterval
        res = []

        i, n = 0, len(intervals)

        while i<n and start>intervals[i][0]:
            res.append(intervals[i])
            i += 1

        if not res or res[-1][1] < start:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], end)

        while i<n:
            start, end = intervals[i]
            i += 1
            if res[-1][1] < start:
                res.append([start, end])
            else:
                res[-1][1] = max(res[-1][1], end)

        return res

