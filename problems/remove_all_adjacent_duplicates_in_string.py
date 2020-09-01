class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return []
        res = [S[0]]
        for cur in S[1:]:
            if res and cur == res[-1]:
                res.pop()
            else:
                res.append(cur)
        return ''.join(res)
