class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        length = len(indices)
        unsorted = []

        for i in range(length):
            unsorted.append([indices[i], s[i]])

        sorteds = sorted(unsorted)

        return ''.join([s[1] for s in sorteds])
