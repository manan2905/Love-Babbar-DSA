# https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        self.pstack = []
        self.minstack = []

    def push(self, val: int) -> None:
        self.pstack.append(val)
        if len(self.minstack) == 0:
            self.minstack.append(val)
        else:
            if val <= self.minstack[-1]:
                self.minstack.append(val)

    def pop(self) -> None:
        d = self.pstack.pop()
        if d == self.minstack[-1]:
            self.minstack.pop()
        return d

    def top(self) -> int:
        return self.pstack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
