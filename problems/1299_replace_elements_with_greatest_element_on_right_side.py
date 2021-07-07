class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """

        maximum = 0

        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]
            arr[i] = maximum
            if tmp > maximum:
                maximum = tmp

        arr[len(arr) - 1] = -1
        return arr
