class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        # dp[i][0] = buy
        # dp[i][1] = sell
        dp = [[0, 0] for _ in range(n + 2)]

        maxBuy = float("-inf")
        maxSell = 0

        for i in range(2, n + 2):
            price = prices[i - 2]

            # Your recurrence
            dp[i][0] = max(dp[i - 2][1], maxSell) - price
            maxBuy = max(maxBuy, dp[i][0])

            dp[i][1] = max(dp[i][0], maxBuy) + price
            maxSell = max(maxSell, dp[i-2][1])

        print("Day  Price   Buy   Sell")
        for i in range(2, n + 2):
            print(f"{i-2:3} {prices[i-2]:6} {dp[i][0]:5} {dp[i][1]:5}")

        return max(maxSell, dp[-2][1], dp[-1][1])