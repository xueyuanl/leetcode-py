class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """

        r_count = 0
        l_count = 0
        res = 0
        for byte in s:
            if byte == 'R':
                r_count += 1
            if byte == 'L':
                l_count += 1
            if r_count == l_count:
                res += 1

        return res
