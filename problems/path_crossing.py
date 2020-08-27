class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """

        s = set()
        x, y = 0, 0
        s.add((x, y))
        for p in path:
            if p == 'N':
                y += 1
            elif p == 'E':
                x += 1
            elif p == 'S':
                y -= 1
            elif p == 'W':
                x -= 1

            if (x, y) in s:
                return True
            else:
                s.add((x, y))
        return False


