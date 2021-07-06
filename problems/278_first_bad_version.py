# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = n
        while a < b:
            mid = int((a + b) / 2)
            is_bad = isBadVersion(mid)
            if not is_bad:
                a = mid + 1
            else:
                b = mid

        return a



