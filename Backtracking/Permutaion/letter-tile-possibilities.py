# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Letter Tile Possibilities): https://leetcode.com/problems/letter-tile-possibilities/
# Tags: Backtracking, DFS, Permutations, Pruning

from typing import List

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        """
        Given a string tiles representing the letters on tiles, return the number of possible non-empty sequences of letters you can make.

        Args:
            tiles (str): A string of uppercase English letters.

        Returns:
            int: Total number of possible non-empty sequences.
        """

        tiles_list = sorted(list(tiles))   # Sort to help with duplicate skipping
        cnt = 0                            # Counter for sequences
        cur = []                           # Current path (not strictly necessary here)
        used = [False] * len(tiles_list)   # Track used indices to avoid repetition

        def dfs(idx):
            nonlocal cnt
            cnt += 1  # Count current permutation

            for i in range(len(tiles_list)):
                if used[i]:
                    continue
                # Skip duplicates (only choose first unused char of duplicate group)
                if i > 0 and tiles_list[i] == tiles_list[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                cur.append(tiles_list[i])   # Choose a letter
                dfs(i)                      # Recurse
                cur.pop()                   # Backtrack
                used[i] = False             # Mark as unused for next loop

        dfs(0)
        return cnt - 1  # Subtract 1 to exclude empty sequence
