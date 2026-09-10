class Solution:
    def calPoints(self, operations: List[str]) -> int:
        print(operations)
        res = []
        ops = operations[::-1]
        op_list = ['+','D','C']
        while len(ops) != 0:
            print(res)
            if ops[-1] not in op_list:
                res.append(int(ops.pop()))
            elif ops[-1] == '+':
                ops.pop()
                a = res.pop()
                b = res.pop()
                new_score = a + b
                res.append(b)
                res.append(a)
                res.append(new_score)
            elif ops[-1] == 'C':
                ops.pop()
                res.pop()
            elif ops[-1] == 'D':
                ops.pop()
                a = res.pop()
                res.append(a)
                res.append(2*a)
            print
        return sum(res)