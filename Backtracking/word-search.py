# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Word Search): https://leetcode.com/problems/word-search/
# Tags: Backtracking, DFS, Recursion, Matrix

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Given an m x n grid of characters `board` and a string `word`, return true if `word` exists in the grid.
        The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
        The same letter cell may not be used more than once.

        Args:
            board (List[List[str]]): 2D grid of characters.
            word (str): Word to search in the board.

        Returns:
            bool: True if the word exists in the board, False otherwise.
        """

        ROWS, COLS = len(board), len(board[0])
        visited = set()  # Tracks visited cells during DFS

        def dfs(r: int, c: int, idx: int) -> bool:
            """
            Depth-first search from position (r, c) to match the word starting from index `idx`.

            Args:
                r (int): Row index.
                c (int): Column index.
                idx (int): Current character index in `word`.

            Returns:
                bool: True if remaining word can be matched starting from (r, c), False otherwise.
            """
            # Base case: All characters matched
            if idx == len(word):
                return True

            # Out of bounds or already visited or character mismatch
            if (
                r < 0 or c < 0 or r >= ROWS or c >= COLS or
                (r, c) in visited or board[r][c] != word[idx]
            ):
                return False

            # Choose the current cell and mark as visited
            visited.add((r, c))

            # Explore neighbors in 4 directions
            res = (
                dfs(r + 1, c, idx + 1) or
                dfs(r - 1, c, idx + 1) or
                dfs(r, c + 1, idx + 1) or
                dfs(r, c - 1, idx + 1)
            )

            # Backtrack
            visited.remove((r, c))

            return res

        # Start DFS from each cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True

        return False
