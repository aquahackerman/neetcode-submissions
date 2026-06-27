class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)

        # dp[i][a] = number of ways to make amount 'a'
        # using the first i coins (coins[0] ... coins[i-1])
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # There is exactly one way to make amount 0:
        # choose no coins.
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            coin = coins[i - 1]
            for a in range(amount + 1):

                # Don't use this coin
                dp[i][a] = dp[i - 1][a]

                # Use this coin (can use it again)
                if a >= coin:
                    dp[i][a] += dp[i][a - coin]

        return dp[n][amount]