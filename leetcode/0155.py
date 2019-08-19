class MinStack:
    stack = []
    monoSeq = []
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.monoSeq = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.monoSeq) == 0 or self.monoSeq[-1] >= x:
            self.monoSeq.append(x)

    def pop(self) -> None:
        tmp = self.stack.pop()
        if self.monoSeq[-1] == tmp:
            self.monoSeq.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.monoSeq[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
