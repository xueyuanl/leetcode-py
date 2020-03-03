class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: bool
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
            if count > 1:
                return False
        return True
