# time O(1)
# space O(1)
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.lead = -1

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.lead += 1

    def pop(self) -> None:
        self.lead -= 1
        del self.stack[self.lead+1]

    def top(self) -> int:
        if self.stack == []:
            return 
        return self.stack[self.lead]

    def getMin(self) -> int:
        if self.stack == []:
            return 
        return min(self.stack)
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()