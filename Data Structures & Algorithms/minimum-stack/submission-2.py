class MinStack:

    def __init__(self):
        self.data = collections.deque()
        self.m = collections.deque([float('inf')])
        

    def push(self, val: int) -> None:
        self.data.append(val)
        if val <= self.m[-1]:
            self.m.append(val)
        

    def pop(self) -> None:
        if self.data[-1] == self.m[-1]:
            self.m.pop()
        return self.data.pop()
        

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.m[-1]
        
