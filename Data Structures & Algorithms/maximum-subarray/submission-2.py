class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l,r,m = 0,0, nums[0]
        for i, no in enumerate(nums):
            l = l + nums[i]
            r = r + nums[len(nums) - i - 1]
            print(r)
            
            m = max(m, max(l,r))
            l = max(0, l)
            r = max(0, r)
        return m