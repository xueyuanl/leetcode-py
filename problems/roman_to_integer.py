class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        res = 0
        i = 0
        le = len(s)
        while i < le:
            if i < le - 1:
                if d[s[i]] >= d[s[i + 1]]:
                    res += d[s[i]]
                else:
                    res += d[s[i + 1]] - d[s[i]]
                    i += 1
            else:
                res += d[s[i]]

            i += 1
        return res