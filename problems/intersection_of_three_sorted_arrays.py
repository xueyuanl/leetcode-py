class Solution(object):
    def arraysIntersection(self, arr1, arr2, arr3):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :type arr3: List[int]
        :rtype: List[int]
        """
        d = {}
        for i in range(len(arr1)):
            s = str(arr1[i])
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1

        for i in range(len(arr2)):
            s = str(arr2[i])
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1

        for i in range(len(arr3)):
            s = str(arr3[i])
            if s not in d:
                d[s] = 1
            else:
                d[s] += 1

        res = []
        for k in d:
            if d[k] >= 3:
                res.append(int(k))
        return sorted(res)