class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        n = target[-1]
        res = []
        target_index = 0
        for i in range(1, n + 1):
            if target[target_index] == i:
                res.append('Push')
                target_index += 1
            else:
                res.append('Push')
                res.append('Pop')
        return res