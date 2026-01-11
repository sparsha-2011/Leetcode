# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Surrounded Regions): https://leetcode.com/problems/surrounded-regions/
# Tags: DFS, Graph, Matrix, Flood Fill, Recursion

from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Modifies the input board in-place by flipping all 'O's that are completely 
        surrounded by 'X's to 'X'. 'O's connected to the border are not flipped.
        """

        ROWS, COLS = len(board), len(board[0])

        def capture(r, c):
            # Base case: if out of bounds or not an 'O', return
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O"):
                return
            # Temporarily mark safe 'O's as 'T'
            board[r][c] = "T"
            # Recurse in all four directions
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        # Step 1: Mark all 'O's connected to the border as safe ('T')
        for r in range(ROWS):
            if board[r][0] == "O":
                capture(r, 0)
            if board[r][COLS - 1] == "O":
                capture(r, COLS - 1)
        
        for c in range(COLS):
            if board[0][c] == "O":
                capture(0, c)
            if board[ROWS - 1][c] == "O":
                capture(ROWS - 1, c)

        # Step 2: Flip all remaining 'O's to 'X' and revert 'T' back to 'O'
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"  # Captured
                elif board[r][c] == "T":
                    board[r][c] = "O"  # Revert safe ones
