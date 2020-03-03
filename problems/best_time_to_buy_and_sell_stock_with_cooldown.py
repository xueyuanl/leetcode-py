
class Solution(object):
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
    """

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0

        s0 = [0] * length
        s1 = [0] * length
        s2 = [0] * length
        s1[0] = -prices[0]
        s2[0] = -1000000

        for i in range(1, length):
            s0[i] = max(s0[i - 1], s2[i - 1])
            s1[i] = max(s1[i - 1], s0[i - 1] - prices[i])
            s2[i] = s1[i - 1] + prices[i]

        return max(s0[length - 1], s2[length - 1])
