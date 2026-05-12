class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #stack implementation 
        stack =[]
        operations = ('+','-','*','/')
        a = 0
        b = 0
        for i in tokens:
            if i not in operations:
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == '+':
                    stack.append(a + b)
                if i == '-':
                    stack.append(a - b)
                if i == '*':
                    stack.append(a * b)
                if i == '/':
                    stack.append(a / b)
        return int(stack.pop())