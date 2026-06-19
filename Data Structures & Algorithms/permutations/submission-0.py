class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(remaining, subset):
            if not remaining:
                res.append(subset)
                return

            for i in range(len(remaining)):
                dfs(
                    remaining[:i] + remaining[i + 1:],
                    subset + [remaining[i]]
                )

        dfs(nums, [])
        return res