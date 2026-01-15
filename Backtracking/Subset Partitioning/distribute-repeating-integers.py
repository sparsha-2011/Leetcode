# Author: Sparsha Srinath
# Date: 2025-08-13
# Problem: Distribute Repeating Integers
# Link: https://leetcode.com/problems/distribute-repeating-integers/
# Tags: Backtracking, Hash Map, Sorting, Pruning
# Time Complexity: Exponential in len(quantity) (backtracking with pruning)
# Space Complexity: O(n) for frequency map + recursion stack

from collections import defaultdict
from typing import List

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        
        freq = defaultdict(int)
        
        quantity.sort(reverse=True)
        for i in nums:
            freq[i] += 1
        
        def backtrack(i):
            if i == len(quantity):
                return True
            
            for k, v in freq.items():
                if freq[k] >= quantity[i]:
                    freq[k] -= quantity[i]
                    if backtrack(i + 1):
                        return True
                    freq[k] += quantity[i]
                
            return False
        
        return backtrack(0)
