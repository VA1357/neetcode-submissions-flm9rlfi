import math

class MinStack:

    #the key is its a min stack from only one direction so keep track of min seen so far and use that
    #since its a stack everything only moves back 1 during a pop or forward one so dont need an index
    def __init__(self):
        self.stack = []
        self.link = []
        self.mini = math.inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.mini:
            self.mini = val
        self.link.append(self.mini)

    def pop(self) -> None:
        self.stack.pop()
        self.link.pop()
        if self.link:
            self.mini = self.link[-1]
        else:
            self.mini = math.inf

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.link[-1]
