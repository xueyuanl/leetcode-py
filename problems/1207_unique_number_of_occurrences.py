class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        s_arr = sorted(arr)

        s = set()

        tmp = 1
        for i in range(1, len(s_arr)):
            if s_arr[i] == s_arr[i - 1]:
                tmp += 1
            else:
                if tmp in s:
                    return False
                else:
                    s.add(tmp)
                    tmp = 1

        if tmp in s:
            return False
        return True


