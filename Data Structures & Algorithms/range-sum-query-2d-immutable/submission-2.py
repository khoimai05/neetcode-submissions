class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        # prefix has one extra row and column of zeros as padding
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for i in range(rows):
            for j in range(cols):
                self.prefix[i+1][j+1] = (
                    matrix[i][j]
                    + self.prefix[i][j+1]     # sum from the row above
                    + self.prefix[i+1][j]     # sum from the col to the left
                    - self.prefix[i][j]       # avoid double-counting overlap
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # shift indices by +1 to account for padding
        r1, c1, r2, c2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return (
            self.prefix[r2][c2]
            - self.prefix[r1-1][c2]
            - self.prefix[r2][c1-1]
            + self.prefix[r1-1][c1-1]
        )