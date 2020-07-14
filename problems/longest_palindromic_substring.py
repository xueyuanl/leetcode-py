class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        dp = [[False] * l for _ in range(l)]
        res = ''

        for i in range(l - 1, -1, -1):
            for j in range(i, l):
                dp[i][j] = s[i] == s[j] and (j - i < 3 or dp[i + 1][j - 1])

                if dp[i][j] and j - i + 1 > len(res):
                    res = s[i:j + 1]
        return res
