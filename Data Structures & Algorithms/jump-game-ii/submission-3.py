from heapq import heappush, heappop

class Solution:
    def jump(self, nums):
        heap = []
        if len(nums) == 1:
            return 0
        # (jumps, furthest_reach)
        heappush(heap, (1, nums[0]))

        for i in range(1, len(nums)):
            while heap and heap[0][1] < i:
                heappop(heap)

            jumps, _ = heap[0]

            heappush(heap, (jumps + 1, i + nums[i]))

        return heap[0][0]