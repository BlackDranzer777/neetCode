s = "()[]{}}"

closing_brackets = {'}':'{', ')':'(', ']':'['}
stack = []

for c in s:
    if c in closing_brackets:
        if len(stack)!=0 and closing_brackets[c] == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
    else:
        stack.append(c)

if len(stack)==0:
    print(True)
else: 
    print(False)