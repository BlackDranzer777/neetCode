class MinStack:

    def __init__(self):
        self.marker = -1
        self.stack = []
        self.minStack = []
        
    # [-2,0,-1]
    def push(self, val: int) -> None:
        if self.marker == -1:
            self.stack.append(val)
            self.minStack.append(val)
        else:
            self.stack.append(val)
            if(val < self.minStack[self.marker]):
                self.minStack.append(val)
            else:
                self.minStack.append(self.minStack[self.marker])
        self.marker+=1

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        self.marker-=1
        

    def top(self) -> int:
        return self.stack[self.marker]
    
    def getMin(self) -> int:
        return self.minStack[self.marker]
    
obj1 = MinStack()
obj1.push(-2)
obj1.push(0)
obj1.push(-1)
# obj1.push(0)
print(obj1.top())
print(obj1.getMin())

