class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # dict of boxes
        # dict of rows
        # dict of cols
        rows_dict = defaultdict(list)
        cols_dict = defaultdict(list)
        boxs_dict = defaultdict(list)   #index by (rows//3, cols//3)
        for i in range(len(board)):
            # print(board[i])
            for j in range(len(board[0])):
                # print(board[i][j])
                # check for row
                if board[i][j] == '.':
                    continue
                if int(board[i][j]) <1 or int(board[i][j]) >9:
                    print(f'{i} {j}')
                    print('here')
                    return False
                if board[i][j] not in rows_dict[i]:
                    rows_dict[i].append(board[i][j])
                else:
                    print(f'{i} {j}')
                    print('here1')
                    return False
                if board[i][j] not in cols_dict[j]:
                    cols_dict[j].append(board[i][j])
                else:
                    print(f'{i} {j}')
                    print('here2')
                    return False
                if  board[i][j] not in boxs_dict[(i//3,j//3)]:
                    boxs_dict[(i//3,j//3)].append(board[i][j])
                else:
                    print(f'{i} {j}')
                    print(f'{i//3} {j//3}')
                    print(board[i][j])
                    print(boxs_dict[(i//3,j//3)])
                    print('here3')
                    return False
        print(rows_dict)
        print(cols_dict)
        print(boxs_dict)
            
        return True