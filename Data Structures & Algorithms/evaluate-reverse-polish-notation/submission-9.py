class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops_list = ['+', '-','*','/']
        res = []
        for i in tokens:
            if i not in ops_list:
                res.append(int(i))
            elif i == '+':
                a = res.pop()
                b = res.pop()
                res.append(b+a)
            elif i == '-':
                a = res.pop()
                b = res.pop()
                res.append(b-a)
            elif i == '*':
                a = res.pop()
                b = res.pop()
                res.append(b*a)                
            elif i == '/':
                a = res.pop()
                b = res.pop()
                res.append(int(b/a))
        return res[-1]
