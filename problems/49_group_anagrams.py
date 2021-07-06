class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        d = {}
        res = []
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in d:
                d[sorted_s].append(s)
            else:
                d[sorted_s] = [s]

        for v in d.values():
            res.append(v)
        return res
    