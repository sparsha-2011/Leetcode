# Author: Sparsha Srinath
# Date: 2025-04-30
# URL: https://leetcode.com/problems/verifying-an-alien-dictionary/
# Tags: strings, hashmap, lexicographical-order, comparison

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Create a mapping of character to its index in the alien dictionary
        order_map = {char: i for i, char in enumerate(order)}

        # Compare each adjacent pair of words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # Edge case: longer word comes before its prefix (e.g., "apple" before "app")
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return False

            # Compare character by character
            for j in range(minLen):
                if w1[j] != w2[j]:
                    # If the characters are in the wrong order, return False
                    if order_map[w1[j]] > order_map[w2[j]]:
                        return False
                    break  # Once a difference is found, no need to check further

        return True
