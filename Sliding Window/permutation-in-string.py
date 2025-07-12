# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/permutation-in-string/
# Tags: Sliding Window, Hash Map, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1) — bounded by fixed alphabet size (26 lowercase letters)

from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Returns True if any permutation of s1 is a substring of s2.

        Args:
            s1 (str): Pattern string whose permutation is to be matched.
            s2 (str): Text string in which to search.

        Returns:
            bool: True if a permutation of s1 exists in s2, False otherwise.
        """
        s1_freq = defaultdict(int)
        for c in s1:
            s1_freq[c] += 1

        k = len(s1)
        count = len(s1_freq)
        start = 0

        for end in range(len(s2)):
            if s2[end] in s1_freq:
                s1_freq[s2[end]] -= 1
                if s1_freq[s2[end]] == 0:
                    count -= 1

            # When window size hits the target
            if end - start + 1 == k:
                if count == 0:
                    return True

                # Slide the window
                if s2[start] in s1_freq:
                    if s1_freq[s2[start]] == 0:
                        count += 1
                    s1_freq[s2[start]] += 1
                start += 1

        return False
