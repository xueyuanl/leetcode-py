class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        a_sorted = sorted(A)

        for i in range(len(a_sorted)):
            if a_sorted[i] == a_sorted[i + 1]:
                return a_sorted[i]

    # set solution
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        s = set()

        for num in A:
            if num in s:
                return num
            else:
                s.add(num)