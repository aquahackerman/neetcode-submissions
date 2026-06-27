
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)

        # rows -> coins considered
        # cols -> amount
        dp = [[0] * (amount + 1) for _ in range(n)]

        # Base case
        for i in range(n):
            dp[i][0] = 1

        for i in range(n):
            coin = coins[i]

            for a in range(1, amount + 1):

                # Propagate from above
                if i > 0:
                    dp[i][a] = dp[i - 1][a]

                # Your idea:
                # if current coin fits, subtract it and
                # look up the SAME COLUMN (same row in the DP)
                if a >= coin:
                    dp[i][a] += dp[i][a - coin]

       

        return dp[n - 1][amount]