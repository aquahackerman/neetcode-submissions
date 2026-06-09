class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            multi = 1
            for j, number in enumerate(nums):
                if j != i:
                    multi *= number
            res.append(multi)
        return res
