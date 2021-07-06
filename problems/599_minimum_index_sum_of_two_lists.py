class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        d = {}
        for i, v in enumerate(list1):
            if v not in d:
                d[v] = i
        sort_list = []
        for i, v in enumerate(list2):
            if v in d:
                sort_list.append([i + d[v], v])

        sort_list.sort()
        res = [sort_list[0][1]]
        for i in range(1, len(sort_list)):
            if sort_list[i][0] == sort_list[i - 1][0]:
                res.append(sort_list[i][1])
            else:
                break

        return res