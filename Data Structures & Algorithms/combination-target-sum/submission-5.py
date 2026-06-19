class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
   
        

        def dfs(i, total, subset):
            
            if i >= len(nums):
                return
            elif nums[i] + total == target:
                subset.append(nums[i])
                res.append(subset.copy())
                subset.pop()
                dfs(i + 1, total, subset)
                return
            elif nums[i] + total >= target:
                dfs(i + 1, total, subset)
                return
            
            no = nums[i]
            subset.append(nums[i])
            print(nums[i], total, subset)
            dfs(i, total + nums[i], subset)
            subset.pop()
            dfs(i+1, total, subset)

        dfs(0, 0, [])
        return res