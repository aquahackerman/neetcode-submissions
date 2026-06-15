class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        m = 0
        if nums[l] <= nums[r]:
            return nums[l]
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                if nums[m] < nums[l]:
                    r = m
                else:
                    l = m + 1
        return nums[m]