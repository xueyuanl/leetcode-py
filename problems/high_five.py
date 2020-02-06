class Solution(object):
    def highFive(self, items):
        """
        :type items: List[List[int]]
        :rtype: List[List[int]]
        """

        d = {}
        for i in items:
            if i[0] in d:
                d[i[0]].append(i[1])
            else:
                d[i[0]] = [i[1]]

        res = []
        for k in d:
            d[k].sort(reverse=True)
            res.append([k, sum(d[k][:5]) / 5])

        return res