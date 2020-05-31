class Solution(object):
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        t_l = len(target)
        a_l = len(arr)
        if t_l != a_l:
            return False
        t_sorted = sorted(target)
        a_sorted = sorted(arr)
        for i in range(t_l):
            if t_sorted[i] != a_sorted[i]:
                return False

        return True
