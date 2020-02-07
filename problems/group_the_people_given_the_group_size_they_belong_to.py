class Solution(object):
    def groupThePeople(self, groupSizes):
        """
        :type groupSizes: List[int]
        :rtype: List[List[int]]
        """

        d = {}
        res = []
        for user in range(len(groupSizes)):
            group = groupSizes[user]
            if group not in d:
                d[group] = []

            d[group].append(user)
            if len(d[group]) == group:
                res.append(d[group][:])
                d[group] = []

        return res
