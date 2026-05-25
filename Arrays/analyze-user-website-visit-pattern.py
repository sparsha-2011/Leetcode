# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/analyze-user-website-visit-pattern/
# Date: 2026-05-24
# Tags: arrays, hash-map, sorting, combinatorics
# Description:
#   Given usernames, timestamps, and websites visited, find the 3-sequence
#   pattern visited by the most users. Group visits by user, sort by timestamp,
#   generate all 3-combinations per user (deduplicated), count patterns across
#   all users, and return the highest-scoring pattern (lexicographically smallest
#   on tie). Tuples compare lexicographically in Python so pattern < best_pattern
#   handles tie-breaking naturally.
#
# Input: username (List[str]), timestamp (List[int]), website (List[str])
# Output: List[str] — the most common 3-sequence pattern
#
# Example:
#   Input : username=["joe","joe","joe","james","james","james","james","mary","mary","mary"]
#           timestamp=[1,2,3,4,5,6,7,8,9,10]
#           website=["home","about","career","home","cart","maps","home","home","about","career"]
#   Output: ["home","about","career"]
#
# Time Complexity : O(U * n³) where U = users, n = max visits per user
# Space Complexity: O(U * n³) for storing all patterns

from typing import List
from collections import defaultdict

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        users = defaultdict(list)
        for u, w, t in zip(username, website, timestamp):
            users[u].append((t, w))

        for user in users:
            users[user].sort()

        pattern_count = defaultdict(int)

        for u in users:

            websites = [w for t, w in users[u]]

            patterns = set()

            for i in range(len(websites)):
                for j in range(i + 1, len(websites)):
                    for k in range(j + 1, len(websites)):
                        patterns.add((websites[i], websites[j], websites[k]))

            for pattern in patterns:
                pattern_count[pattern] += 1

        best_pattern = None
        best_count = 0
        for pattern, count in pattern_count.items():
            if count > best_count:
                best_count = count
                best_pattern = pattern
            elif count == best_count:
                if pattern < best_pattern:
                    best_pattern = pattern
        return list(best_pattern)
