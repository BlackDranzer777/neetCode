# tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
class Solution:

    def __init__(self):
        self.marker1=0
        self.marker2=1
        self.operators = {'+','-','*', '/'}
        self.stack=[]
        self.stack.append(self.marker1)
        self.stack.append(self.marker2)

    def evalRPN(self, tokens: List[str]) -> int:
        for i in range(2,tokens):
            if i in self.operators:
                if i=='+':
                    self.stack[self.marker1] = self.stack[self.marker1] + self.stack[self.marker2]
                elif i=='/':
                    self.stack[self.marker1] = self.stack[self.marker1] + self.stack[self.marker2]
                elif i=='-':
                    self.stack[self.marker1] = self.stack[self.marker1] + self.stack[self.marker2]
                elif i=='*':
                    self.stack[self.marker1] = self.stack[self.marker1] + self.stack[self.marker2]
            else:
                self.stack.append(i)
                self.marker1 +=1
                self.marker2 +=1

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
obj1 = Solution(tokens)