# Date: 2025-05-28
# Author: Sparsha Srinath
# LeetCode: https://leetcode.com/problems/sudoku-solver/
# Tags: Backtracking, Constraint Propagation
# Problem: 37. Sudoku Solver
# Description:
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# - Each of the digits 1-9 must occur exactly once in each row.
# - Each of the digits 1-9 must occur exactly once in each column.
# - Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes.

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Preprocess the board
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empty.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[3 * (r // 3) + (c // 3)].add(val)

        def backtrack(i):
            if i == len(empty):
                return True  # Solved

            r, c = empty[i]
            b = 3 * (r // 3) + (c // 3)

            for d in '123456789':
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)

                    if backtrack(i + 1):
                        return True

                    board[r][c] = '.'
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)

            return False

        backtrack(0)
