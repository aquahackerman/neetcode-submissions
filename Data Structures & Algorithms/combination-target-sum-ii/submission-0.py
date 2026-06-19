class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        groups = []
        i = 0
        while i < len(candidates):
            j = i
            while j < len(candidates) and candidates[j] == candidates[i]:
                j += 1

            groups.append((candidates[i], j - i))
            i = j

        res = []

        def dfs(idx, total, subset):
            if total == target:
                res.append(subset.copy())
                return

            if total > target or idx == len(groups):
                return

            num, freq = groups[idx]

            # choose 0..freq copies of num
            for take in range(freq + 1):
                for _ in range(take):
                    subset.append(num)

                dfs(idx + 1, total + take * num, subset)

                for _ in range(take):
                    subset.pop()

        dfs(0, 0, [])
        return res