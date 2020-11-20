# Algorithm:
# 1. place queen row by row, scan available spots column by column
# 2. as a new queen is placed, mark indices of occupied column and two diagonals
#    to remove from further consideration
# 3. recursively place the next queen until all queens are placed

class Solution:
    def __init__(self):
        self.n = 0
        self.res = []

    def backtrack(self, row: int, cols: list, dia_left: set, dia_right: set):
        # row: placing a queen at "row"th row
        # cols: sequence of queen's col index, row by row
        # dia_left, dia_right: the set to mark whether a diagonal is occupied

        if row == self.n:
            # we placed all the queens, generate output
            self.res += [["." * c + "Q" + "." * (self.n - c - 1) for c in cols]]
            return

        for col in set(range(self.n)) - set(cols):
            # exclude columns that are already occupied

            dl = col - row
            # diagonal from upper left to lower right.
            # functions of y = x + k => k = y - x
            # horizontally mirrored, since origin(0, 0) is at upper left,
            # and positive toward right and down

            dr = col + row
            # diagonal from lower left to upper right.
            # functions of y = -x + k => k = x + y
            # horizontally mirrored, since origin(0, 0) is at upper left,
            # and positive toward right and down

            if not (dl in dia_left or dr in dia_right):
                # found available queen position,
                # append to queens sequence, add used diagonals,
                # then recursively place the next queen
                self.backtrack(row + 1, cols + [col], dia_left | set([dl]), dia_right | set([dr]))

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        self.res = []
        self.backtrack(0, [], set(), set())
        return self.res