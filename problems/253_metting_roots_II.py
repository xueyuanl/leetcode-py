class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        timeline = []

        for i in intervals:
            timeline.append([i[0], 1])
            timeline.append([i[1], -1])

        s_timeline = sorted(timeline)

        count = 0
        res = 0

        for t in s_timeline:
            count += t[1]
            res = max(res, count)
        return res
