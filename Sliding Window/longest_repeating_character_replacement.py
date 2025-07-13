# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/longest-repeating-character-replacement/
# Tags: Sliding Window, HashMap
# Time Complexity: O(26 * n) => O(n)
# Space Complexity: O(1) — bounded by 26 English uppercase letters
# Description:
#   Given a string `s` and an integer `k`, return the length of the longest substring
#   that can be transformed into a string with all repeating characters by replacing
#   at most `k` characters.

from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        freq = defaultdict(int)
        maxLen = 0

        for end in range(len(s)):
            freq[s[end]] += 1

            # Check if more than k replacements are needed
            while end - start + 1 - max(freq.values()) > k:
                freq[s[start]] -= 1
                start += 1

            maxLen = max(maxLen, end - start + 1)

        return maxLen
