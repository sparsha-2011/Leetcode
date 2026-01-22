# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/minimum-window-substring/
# Tags: Sliding Window, HashMap, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(k), where k is the number of unique characters in `t`
# Description:
#   Given two strings `s` and `t`, return the minimum window in `s` which will contain
#   all the characters in `t`. If no such window exists, return an empty string.

from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = defaultdict(int)
        for c in t:
            freq[c] += 1

        start = 0
        minLen = float('inf')
        minWin = ""
        count = len(freq)

        for end in range(len(s)):
            if s[end] in freq:
                freq[s[end]] -= 1
                if freq[s[end]] == 0:
                    count -= 1

            while count == 0:
                if end - start + 1 < minLen:
                    minLen = end - start + 1
                    minWin = s[start:end + 1]

                if s[start] in freq:
                    if freq[s[start]] == 0:
                        count += 1
                    freq[s[start]] += 1

                start += 1

        return minWin
