class Solution(object):
    """
    https://segmentfault.com/a/1190000003811919
    """
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            for j in range(i):
                dp[i] = dp[i] + dp[j] * dp[i - j - 1]

        return dp[n]

    def f(self, n):
        """
        Time Limit Exceeded method
        """
        if n == 1:
            return 1
        if n == 0:
            return 1
        res = 0
        for i in range(n):
            res += self.f(i) * self.f(n - 1 - i)
        return res
