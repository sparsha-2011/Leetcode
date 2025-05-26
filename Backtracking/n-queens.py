# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (N-Queens): https://leetcode.com/problems/n-queens/
# Tags: Backtracking, DFS, Recursion

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        Solves the N-Queens problem by placing N queens on an N×N chessboard 
        such that no two queens threaten each other.

        Args:
            n (int): Size of the chessboard (n x n)

        Returns:
            List[List[str]]: All distinct solutions as a list of board configurations
        """

        board = [['.'] * n for _ in range(n)]
        res = []

        def isSafe(r: int, c: int) -> bool:
            """
            Checks if a queen can be safely placed at (r, c).

            Args:
                r (int): Row index
                c (int): Column index

            Returns:
                bool: True if it's safe, False otherwise
            """

            # Check row on left
            for j in range(c):
                if board[r][j] == 'Q':
                    return False

            # Check upper diagonal on left
            i, j = r - 1, c - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # Check lower diagonal on left
            i, j = r + 1, c - 1
            while i < n and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j -= 1

            return True

        def dfs(c: int) -> None:
            """
            Uses depth-first search to place queens column by column.

            Args:
                c (int): Current column to attempt placing a queen
            """

            if c == n:
                # All queens placed successfully; store current configuration
                res.append(["".join(row) for row in board])
                return

            for r in range(n):
                if isSafe(r, c):
                    board[r][c] = 'Q'
                    dfs(c + 1)
                    board[r][c] = '.'  # Backtrack

        dfs(0)
        return res
