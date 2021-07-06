class Solution(object):
    def countLetters(self, S):
        """
        :type S: str
        :rtype: int
        """

        length = len(S)
        ans = 0
        repeat = 1
        for i in range(1, length):
            if S[i] != S[i - 1]:
                ans += repeat * (repeat + 1) / 2
                repeat = 0
            repeat += 1
        return ans + repeat * (repeat + 1) / 2