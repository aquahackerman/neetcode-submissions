class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        ends = [intervals[0].end]

        for i in range(1, len(intervals)):
            found = False

            for j in range(len(ends)):
                if intervals[i].start >= ends[j]:
                    ends[j] = intervals[i].end
                    found = True
                    break

            if not found:
                ends.append(intervals[i].end)

        return len(ends)