class Solution(object):
    """
    refer: https://leetcode.jp/leetcode-1079-letter-tile-possibilities-%E8%A7%A3%E9%A2%98%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90/
    """

    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """

        alpha = [0] * 26
        for t in tiles:
            alpha[ord(t) - 65] += 1

        return self.backtracking(alpha)

    def backtracking(self, alpha):
        res = 0

        for i in range(26):
            if alpha[i] == 0:
                continue
            res += 1
            alpha[i] -= 1
            res += self.backtracking(alpha)
            alpha[i] += 1
        return res



