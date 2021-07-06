class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

        self.minstack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

        if not self.minstack:
            self.minstack.append(x)
        elif x <= self.minstack[-1]:
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        popped = self.stack.pop()
        if self.minstack and self.minstack[-1] == popped:
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
