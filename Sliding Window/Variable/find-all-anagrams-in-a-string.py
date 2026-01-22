# Author: Sparsha Srinath
# Date: 2025-06-29
# Leetcode: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Tags: Sliding Window, Hash Map, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1) (constant alphabet size)

from typing import List
from collections import defaultdict

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Finds all start indices of p's anagrams in s.

        Args:
            s (str): The string to search in.
            p (str): The anagram string.

        Returns:
            List[int]: Starting indices of anagrams of p in s.
        """
        result = []
        p_freq = defaultdict(int)
        
        for c in p:
            p_freq[c] += 1
        
        k = len(p)
        count = len(p_freq)  # number of chars to match
        start = 0
        
        for end in range(len(s)):
            if s[end] in p_freq:
                p_freq[s[end]] -= 1
                if p_freq[s[end]] == 0:
                    count -= 1
            
            # When window size reaches k, check anagram condition
            if end - start + 1 == k:
                if count == 0:
                    result.append(start)
                
                # Move start pointer forward, update counts accordingly
                if s[start] in p_freq:
                    if p_freq[s[start]] == 0:
                        count += 1
                    p_freq[s[start]] += 1
                
                start += 1
        
        return result
