# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/longest-common-subsequence/
# Date: 2026-05-25
# Tags: strings, dynamic-programming, 2d-dp
# Description:
#   Given two strings, find the length of the longest common subsequence.
#   A subsequence is a sequence that appears in the same relative order but
#   not necessarily contiguous. Use a 2D DP table where dp[i][j] represents
#   the LCS length of text1[:i] and text2[:j]. If characters match, extend
#   the diagonal (dp[i-1][j-1] + 1). Otherwise, take the max of skipping
#   either character (dp[i-1][j] or dp[i][j-1]).
#
#   Visualization for text1="ace", text2="abcde":
#       ""  a  b  c  d  e
#   ""   0  0  0  0  0  0
#   a    0  1  1  1  1  1
#   c    0  1  1  2  2  2
#   e    0  1  1  2  2  3  → answer: 3
#
# Input: text1 (str), text2 (str)
# Output: int — length of longest common subsequence
#
# Example:
#   Input : text1="abcde", text2="ace"
#   Output: 3 (LCS is "ace")
#
# Time Complexity : O(m * n) where m and n are lengths of the strings
# Space Complexity: O(m * n) for the 2D DP table

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = [[0] * (n + 1) for i in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]
