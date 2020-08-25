class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        # dp[x][y], represent the profit in day-x,
        # dp[x][0], in day-x, has no stock, the profit value
        # dp[x][1], in day-x, has stock, the profit value
        dp = [[0 for i in range(2)] for j in range(len(prices))]

        for i in range(len(prices)):
            if i == 0:  # day1
                dp[i][0] = 0  # no stock, profit is 0
                dp[i][1] = -prices[i]  # in day1, buy stock, profit is negative.
            else:
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], - prices[i])

        return dp[len(prices) - 1][0]

    def maxProfit_s2(self, prices):
        if not prices:
            return 0
        profit_0, profit_1 = 0, -prices[0]
        for i in range(1, len(prices)):
            profit_0 = max(profit_0, profit_1 + prices[i])
            profit_1 = max(profit_1, -prices[i])

        return profit_0
