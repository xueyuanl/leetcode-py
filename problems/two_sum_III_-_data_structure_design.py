class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s = []

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        self.s.append(number)

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        temp = set()
        for s in self.s:
            if value - s in temp:
                return True
            temp.add(s)
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
