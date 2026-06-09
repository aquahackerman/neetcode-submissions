import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        ends = [intervals[0].end]
        heapq.heapify(ends)

        for i in range(1, len(intervals)):
            if intervals[i].start >= ends[0]:
                heapq.heappop(ends)

            heapq.heappush(ends, intervals[i].end)

        return len(ends)