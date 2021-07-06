class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        temp = [0] * 1001
        for item in arr1:
            temp[item] += 1

        res = []
        for item in arr2:
            if temp[item] > 0:
                res.extend([item] * temp[item])
                temp[item] = -1  # mark as used

        to_sort = []
        for item in arr1:
            if temp[item] > 0:  # item in arr1, but not in arr2
                to_sort.append(item)

        res.extend(sorted(to_sort))
        return res
