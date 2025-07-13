# Author: Sparsha Srinath
# Date: 2025-06-29
# URL: https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
# Tags: Sliding Window, HashMap, Strings
# Time Complexity: O(n)
# Space Complexity: O(k)
# Description:
#   Given a string s and an integer k, find the length of the longest substring
#   that contains exactly k unique characters. Return -1 if no such substring exists.

from collections import defaultdict

class Solution:
    def longestKSubstr(self, s: str, k: int) -> int:
        """
        Returns the length of the longest substring with exactly k unique characters.

        Args:
            s (str): Input string.
            k (int): Number of unique characters required.

        Returns:
            int: Length of the longest valid substring, or -1 if none exists.
        """
        start = 0
        unique = defaultdict(int)
        maxLen = 0

        for end in range(len(s)):
            unique[s[end]] += 1

            # Shrink the window if we have more than k unique characters
            while len(unique) > k:
                unique[s[start]] -= 1
                if unique[s[start]] == 0:
                    del unique[s[start]]
                start += 1

            # Check for exactly k unique characters
            if len(unique) == k:
                maxLen = max(maxLen, end - start + 1)

        return maxLen if maxLen > 0 else -1
