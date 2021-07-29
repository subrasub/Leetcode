class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return

        intervals.sort(key = lambda x:x[0])

        rooms = []
        heapq.heappush(rooms, intervals[0][1])

        count = 0

        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])

        return len(rooms)