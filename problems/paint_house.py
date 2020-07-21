class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        length = len(costs)
        if length == 0:
            return 0
        dp = [[0 for i in range(3)] for j in range(length)]

        dp[0][0] = costs[0][0]
        dp[0][1] = costs[0][1]
        dp[0][2] = costs[0][2]

        for i in range(1, length):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]

        return min(dp[length - 1][0], dp[length - 1][1], dp[length - 1][2])

