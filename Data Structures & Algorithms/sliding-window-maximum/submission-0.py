class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = []
        for no in range(0, len(nums) - k + 1):
            l.append(max(nums[no: no + k]))
        return l
