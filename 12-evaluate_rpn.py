from typing import List

class Solution:

    def __init__(self):
        self.operators = {'+','-','*', '/'}
        self.stack=[]

    def evalRPN(self, tokens: List[str]) -> int:
        for i in range(0,len(tokens)):
            if tokens[i] in self.operators:
                if tokens[i]=='+':
                    self.stack.append(self.stack.pop()+ self.stack.pop())
                elif tokens[i]=='/':
                    a, b = self.stack.pop() , self.stack.pop()
                    self.stack.append(int(b/a))
                elif tokens[i]=='-':
                    a,b = self.stack.pop() , self.stack.pop()
                    self.stack.append(b-a)
                elif tokens[i]=='*':
                    self.stack.append(self.stack.pop() * self.stack.pop())
            else:
                self.stack.append(int(tokens[i]))
            print(self.stack)
        return self.stack[0]

tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
obj1 = Solution()
result = obj1.evalRPN(tokens)
print(result)