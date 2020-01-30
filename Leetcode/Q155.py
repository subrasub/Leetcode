class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minS = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minS or x <= self.minS[-1]:
            self.minS.append(x)

    def pop(self) -> None:
        s = self.stack.pop()
        if s==self.minS[-1]:
            self.minS.pop()      

    def top(self) -> int:
        if not self.stack:
            return None
        else:
            return self.stack[-1]

    def getMin(self) -> int:
        if not self.minS:
            return None
        else:
            return self.minS[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
