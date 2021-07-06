class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        res = []

        for a in A:
            for i in range(len(B)):
                if a == B[i]:
                    res.append(i)
                    break

        return res