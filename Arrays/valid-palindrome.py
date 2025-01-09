# Problem Title: Valid Palindrome
# Problem URL: https://leetcode.com/problems/valid-palindrome/
# Difficulty: Easy

"""
Problem Statement:

Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

Example 2:

Input: s = "tab a cat"

Output: false
Explanation: "tabacat" is not a palindrome.

Constraints:

1 <= s.length <= 1000
s is made up of only printable ASCII characters.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Two pointers: one starting from the beginning and one from the end
        l = 0 
        r = len(s) - 1

        # Loop until the two pointers meet
        while l < r:
            # Move the left pointer to the next alphanumeric character
            while l < r and not self.alphaNum(s[l]):
                l += 1
            # Move the right pointer to the previous alphanumeric character
            while l < r and not self.alphaNum(s[r]):
                r -= 1
            # Check if the characters are the same (case insensitive)
            if s[l].lower() != s[r].lower():
                return False
            # Move both pointers inward
            l += 1
            r -= 1
        # If we successfully reached the center, it's a palindrome
        return True

    def alphaNum(self, c):
        # Check if the character is alphanumeric (letters or digits)
        return (ord('A') <= ord(c) <= ord('Z') or 
                ord('a') <= ord(c) <= ord('z') or 
                ord('0') <= ord(c) <= ord('9'))
