class Solution:
  def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    intervals.sort()
    # free rooms
    available = []

    heapq.heappush(available, intervals[0][1])

    for interval in intervals[1:]:
      if available[0] <= interval[0]:
        heapq.heappop(available)
      heapq.heappush(available, interval[1])

    return len(available)