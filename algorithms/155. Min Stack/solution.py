class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = float('inf')
        self.data = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self.min:
            self.data.append(self.min)
            self.min = x
        self.data.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.min == self.data.pop():
            self.min = self.data.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
