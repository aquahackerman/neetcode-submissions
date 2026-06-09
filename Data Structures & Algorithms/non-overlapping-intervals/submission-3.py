class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        arr = sorted(intervals)
        a,b = arr[0][0], arr[0][1]
        count = -1
        for s,e in arr:
            if s >= b:
                a, b = s,e
            else:
                print(s,e,a,b)
                b = min(e,b)

                count += 1
        
        return count
