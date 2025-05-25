# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode (Letter Combinations of a Phone Number): https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Tags: Backtracking, DFS, Recursion, Strings, HashMap

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        Given a string containing digits from 2-9 inclusive, return all possible letter combinations 
        that the number could represent. Return the answer in any order.

        Args:
            digits (str): A string consisting of digits from 2 to 9.

        Returns:
            List[str]: A list of all possible letter combinations.
        """

        # Mapping of digits to letters like on a phone keypad
        num_str = {
            2: 'abc', 3: 'def', 4: 'ghi',
            5: 'jkl', 6: 'mno', 7: 'pqrs',
            8: 'tuv', 9: 'wxyz'
        }

        res = []  # Stores final combinations
        cur = []  # Temporary list to build each combination

        # Edge case: if input is empty, return an empty list
        if not digits:
            return []

        def dfs(idx: int) -> None:
            """
            Performs depth-first search to build all combinations recursively.

            Args:
                idx: Current index in the input digit string
            """
            if idx == len(digits):
                # Full combination formed, add to result
                res.append(''.join(cur))
                return

            # Iterate over the letters mapped to the current digit
            for ch in num_str[int(digits[idx])]:
                cur.append(ch)       # Choose a letter
                dfs(idx + 1)         # Move to next digit
                cur.pop()            # Backtrack

        dfs(0)
        return res
