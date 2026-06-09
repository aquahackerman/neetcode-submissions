class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):
            diff = target - number 
            if diff in seen:
                return [seen[diff],i]
            else:
                seen[number] = i
        return[]
