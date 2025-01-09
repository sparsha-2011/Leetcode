# Problem Title: Valid Anagram
# Problem URL: https://leetcode.com/problems/valid-anagram/
# Difficulty: Easy

"""
Problem Statement:
Given two strings `s` and `t`, return `true` if the two strings are anagrams of each other, 
otherwise return `false`.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Examples:
1. Input: s = "racecar", t = "carrace"
   Output: true

2. Input: s = "jar", t = "jam"
   Output: false

Constraints:
- 1 <= s.length, t.length <= 5 * 10^4
- `s` and `t` consist of lowercase English letters.
"""

from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if two strings are anagrams.

        Args:
        s (str): The first input string.
        t (str): The second input string.

        Returns:
        bool: True if `s` and `t` are anagrams, False otherwise.
        """
        # Frequency counters for both strings
        s_freq = defaultdict(int)
        t_freq = defaultdict(int)

        # Count character frequencies in s
        for char in s:
            s_freq[char] += 1

        # Count character frequencies in t
        for char in t:
            t_freq[char] += 1

        # Compare frequency dictionaries
        return s_freq == t_freq

# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Example Test Case 1
    s = "racecar"
    t = "carrace"
    print(sol.isAnagram(s, t))  # Output: True

    # Example Test Case 2
    s = "jar"
    t = "jam"
    print(sol.isAnagram(s, t))  # Output: False

    # Additional Test Case
    s = "aabbcc"
    t = "ccbbaa"
    print(sol.isAnagram(s, t))  # Output: True

