from typing import List


class Solution:
    def backtrack(self, row: int) -> None:

        if row == self.n:
            solution = ["".join(boardrow) for boardrow in self.board]
            self.res.append(solution)
            return

        for col in range(self.n):
            pos_idx = row + col
            neg_idx = row - col
            if (
                    # col in occupied
                    col in self.occupied_cols
                    or
                    # +diag in occupied
                    pos_idx in self.occupied_pos_diag
                    or
                    # -diag in occupied
                    neg_idx in self.occupied_neg_diag
            ):
                #             skip this col
                continue
            #  mark is occupied
            self.occupied_cols.add(col)
            self.occupied_pos_diag.add(pos_idx)
            self.occupied_neg_diag.add(neg_idx)
            # check if next solution fits
            self.board[row][col] = "Q"
            self.backtrack(row + 1)
            self.board[row][col] = "."
            # unmark occupied
            self.occupied_cols.remove(col)
            self.occupied_pos_diag.remove(pos_idx)
            self.occupied_neg_diag.remove(neg_idx)

    def solveNQueens(self, n: int) -> List[List[str]]:
        self.n = n
        # col
        self.occupied_cols = set()
        # row+col
        self.occupied_pos_diag = set()
        # row-col
        self.occupied_neg_diag = set()

        self.res = []
        self.board = [["."] * n for _ in range(n)]
        self.backtrack(0)

        return self.res
