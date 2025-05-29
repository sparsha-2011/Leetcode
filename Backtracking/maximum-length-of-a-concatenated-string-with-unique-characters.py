# Date: 2025-04-15
# Author: Sparsha Srinath
# Leetcode: https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
# Tags: Backtracking, String, Bit Manipulation (optional optimization)
# Problem: Maximum Length of a Concatenated String with Unique Characters

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        cur = []
        cur_len = 0
        
        # Check if a string has all unique characters
        def is_unique(s):
            return len(s) == len(set(s))

        # Check if a new word has any overlap with current list
        def no_common_letters(current_words, new_word):
            current_chars = set(''.join(current_words))
            return not (set(new_word) & current_chars)

        def dfs(idx):
            nonlocal max_len, cur_len
            max_len = max(max_len, cur_len)

            for i in range(idx, len(arr)):
                word = arr[i]
                if is_unique(word) and no_common_letters(cur, word):
                    cur.append(word)
                    cur_len += len(word)
                    dfs(i + 1)
                    cur.pop()
                    cur_len -= len(word)

        dfs(0)
        return max_len
