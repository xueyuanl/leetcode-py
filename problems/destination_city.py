class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """

        department_set = set()
        destination_set = set()

        for pair in paths:
            department_set.add(pair[0])
            if pair[1] not in department_set:
                destination_set.add(pair[1])
            if pair[0] in destination_set:
                destination_set.discard(pair[0])

        return destination_set.pop()
