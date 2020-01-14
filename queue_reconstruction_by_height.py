class Solution(object):
    """
    best explanation: https://leetcode.com/problems/queue-reconstruction-by-height/discuss/167308/Python-solution
    """

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people_sorted = sorted(people, key=lambda x: (-x[0], x[1]))

        res = []

        for p in people_sorted:
            res.insert(p[1], p)
        return res


if __name__ == '__main__':
    pass
