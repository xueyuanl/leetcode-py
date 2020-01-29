
class Solution(object):
    """
    use mathematical method, but not a good way to understand.
    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        res = 0
        for i in range(1, n):
            # 5 apples given 3 person, there are C(5-1, 3-1) situations.
            res += self.combination(m, i) * self.combination(n - 1 - 1, i - 1)
        return res

    def combination(self, m, n):
        """
        C(m, n). from m, take n, without order
        """
        res = 1
        for i in range(m, m - n, -1):
            res *= i

        nn = 1
        for i in range(n, 0, -1):
            nn *= i

        return int(res / nn)

    # using DP, a better way
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for _ in range(m)] for _ in range(n)]
        print(dp)

        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[-1][-1]
