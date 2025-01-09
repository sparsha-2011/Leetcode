# Problem Title: Encode and Decode Strings
# Problem URL: https://leetcode.com/problems/encode-and-decode-strings/
# Difficulty: Medium

"""
Problem Statement:
Design an algorithm to encode a list of strings to a single string. 
The encoded string should then be decoded back to the original list of strings.

Examples:
1. Input: ["neet", "code", "love", "you"]
   Output: ["neet", "code", "love", "you"]

2. Input: ["we", "say", ":", "yes"]
   Output: ["we", "say", ":", "yes"]

Constraints:
- 0 <= strs.length < 100
- 0 <= strs[i].length < 200
- strs[i] contains only UTF-8 characters
"""

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:

        res = ""
        for w in strs:
            
            res += str(len(w)) + "#" + w
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        print(s)
        res, i = [],0

        while i <len(s):

            j = i
            while s[j] != '#':

                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
            
        return res
