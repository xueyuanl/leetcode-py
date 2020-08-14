class MonotonicQueue(object):
    def __init__(self):
        self.list = []  # a dummy deque
        self.head = 0  # mark the front of the deque
        self.tail = -1

    def get_max(self):
        return self.list[self.head]

    def push(self, n):
        while self.list and self.tail >= self.head and self.list[-1] < n :
            self.tail -= 1
            del self.list[-1]
        self.list.append(n)
        self.tail += 1

    def pop(self, n):
        if self.list and self.list[self.head] == n:
            self.head += 1


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        mq = MonotonicQueue()
        for i in range(0, len(nums)):
            if i < k - 1:
                mq.push(nums[i])
            else:
                mq.push(nums[i])
                if i - k >= 0:
                    mq.pop(nums[i - k])
                res.append(mq.get_max())

        return res
