class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        col_stk = []
        index = 0
        while index < len(asteroids):
            i = asteroids[index]
            if (not col_stk) or (i>0) or (i < 0 and col_stk[-1] < 0):
                col_stk.append(i)
                print(f'append {i} at {index}')
                index+=1
            else:
                if abs(i) > abs(col_stk[-1]):
                    col_stk.pop()
                    # print(col_stk)
                elif abs(i) == abs(col_stk[-1]):
                    # print(col_stk)
                    index+=1
                    col_stk.pop()
                else:
                    index+=1
        return col_stk