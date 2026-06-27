class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        n = len(coins)
        if amount == 0:
            return 1
        # dp[amount][coin_index]
        dp = [[0] * (n + 1) for _ in range(amount + 1)]

        for a in range(amount + 1):
            for j in range(1, n + 1):
                coin = coins[j - 1]

                if a < coin:
                    dp[a][j] = dp[a][j - 1]

                elif a == coin:
                    dp[a][j] = 1 + dp[a][j - 1]

                else:
                    dp[a][j] = dp[a][j - 1] + dp[a - coin][j]

        

        return dp[amount][n]