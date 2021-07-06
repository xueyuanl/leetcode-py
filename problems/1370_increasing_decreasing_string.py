class Solution(object):
    def sortString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        res = []

        while s:
            for l in sorted(set(s)):
                s.remove(l)
                res.append(l)
            for l in sorted(set(s), reverse=True):
                s.remove(l)
                res.append(l)
        return ''.join(res)
