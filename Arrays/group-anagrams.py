# Problem Title: Group Anagrams
# Problem URL: https://leetcode.com/problems/group-anagrams/
# Difficulty: Medium

"""
Problem Statement:
Given an array of strings `strs`, group all anagrams together into sublists. 
You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, 
but the order of the characters can be different.

Examples:
1. Input: strs = ["act", "pots", "tops", "cat", "stop", "hat"]
   Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]

2. Input: strs = ["x"]
   Output: [["x"]]

3. Input: strs = [""]
   Output: [[""]]

Constraints:
- 1 <= strs.length <= 1000
- 0 <= strs[i].length <= 100
- strs[i] is made up of lowercase English letters.
"""

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups strings into lists of anagrams.

        Args:
        strs (List[str]): The list of input strings.

        Returns:
        List[List[str]]: A list of lists, where each sublist contains anagrams.
        """
        anagram_set = defaultdict(list)

        for i in strs:
            val = [0] * 26
            for j in i:
                val[ord(j) - ord('a')] += 1 
            
            anagram_set[tuple(val)].append(i)
        
        return list(anagram_set.values())

# Test Cases
if __name__ == "__main__":
    sol = Solution()

    # Example Test Case 1
    strs = ["act", "pots", "tops", "cat", "stop", "hat"]
    print(sol.groupAnagrams(strs))  # Output: [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]

    # Example Test Case 2
    strs = ["x"]
    print(sol.groupAnagrams(strs))  # Output: [["x"]]

    # Example Test Case 3
    strs = [""]
    print(sol.groupAnagrams(strs))  # Output: [[""]]

    # Additional Test Case
    strs = ["a", "b", "ab", "ba"]
    print(sol.groupAnagrams(strs))  # Output: [["a"], ["b"], ["ab", "ba"]]
