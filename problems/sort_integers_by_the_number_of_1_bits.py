class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def count_bits(n):
            count = 0
            while n > 0:
                if n & 1 == 1:
                    count += 1
                n = n >> 1
            return count
        s = [[] for i in range(14)]

        for item in arr:
            number = count_bits(item)
            s[number].append(item)

        res = []
        for i in s:
            if i:
                res.extend(sorted(i))
        return res

