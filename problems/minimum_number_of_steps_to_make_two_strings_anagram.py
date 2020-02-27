class Solution(object):
    def minSteps(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        array_s = [0] * 26
        array_t = [0] * 26

        for ch in s:
            array_s[ord(ch) - 97] += 1

        for ch in t:
            array_t[ord(ch) - 97] += 1

        count = 0
        for i in range(26):
            if array_s[i] > array_t[i]:
                count += array_s[i] - array_t[i]

        return count
