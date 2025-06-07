# Date: 2025-05-28
# Author: Sparsha Srinath
# Leetcode (Palindrome Partitioning): https://leetcode.com/problems/palindrome-partitioning/
# Tags: Backtracking, DFS, Strings

from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        Generates all possible palindrome partitionings of the input string.

        Args:
            s (str): The input string.

        Returns:
            List[List[str]]: A list of all partitions where each substring is a palindrome.
        """

        res = []
        cur = []

        def dfs(idx: int):
            # If we reach the end of the string, record the current partition
            if idx == len(s):
                res.append(cur.copy())
                return
            
            for i in range(idx, len(s)):
                sub_str = s[idx:i+1]

                # Check if the current substring is a palindrome
                if sub_str == sub_str[::-1]:
                    cur.append(sub_str)
                    dfs(i + 1)
                    cur.pop()

        dfs(0)
        return res
