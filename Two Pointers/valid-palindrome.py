# Author: Sparsha Srinath
# Date: 2025-06-29
# Problem: Valid Palindrome
# Source: Leetcode - https://leetcode.com/problems/valid-palindrome/
# Tags: Two Pointers, String
# Time Complexity: O(n), where n is the length of the string
# Space Complexity: O(1), constant extra space

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()  # Convert to lowercase for case-insensitive comparison

        while l < r:
            # Skip non-alphanumeric characters from the left
            if not s[l].isalnum():
                l += 1
                continue

            # Skip non-alphanumeric characters from the right
            if not s[r].isalnum():
                r -= 1
                continue

            # Compare characters
            if s[l] != s[r]:
                return False

            l += 1
            r -= 1

        return True  # All matched, it's a palindrome
