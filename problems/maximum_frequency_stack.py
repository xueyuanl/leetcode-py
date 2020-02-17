import heapq


class FreqStack(object):

    def __init__(self):
        self.freq = {}
        self.priority_q = []
        self.index = 0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x in self.freq:
            self.freq[x] += 1
        else:
            self.freq[x] = 1
        heapq.heappush(self.priority_q, (-self.freq[x], -self.index, x))
        self.index += 1

    def pop(self):
        """
        :rtype: int
        """
        val = heapq.heappop(self.priority_q)[2]
        self.freq[val] -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()