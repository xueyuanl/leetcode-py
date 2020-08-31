class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.sum = 0
        self.list = []
        self.size = size

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        if len(self.list) > self.size:
            self.sum -= self.list[-self.size]
        self.sum += val
        self.list.append(val)
        return float(self.sum / self.size)

# class MovingAverage(object):
#
#     def __init__(self, size):
#         """
#         Initialize your data structure here.
#         :type size: int
#         """
#         self.queue = collections.deque(maxlen=size)
#
#     def next(self, val):
#         """
#         :type val: int
#         :rtype: float
#         """
#         queue = self.queue
#         queue.append(val)
#         return float(sum(queue)) / len(queue)
