
# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/alien-dictionary/
# Date: 2025-04-23
# Tags: topological-sort, graphs, strings, kahn's-algorithm

from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Step 1: Initialize graph and indegree map
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for w in words for c in w}

        # Step 2: Build graph from adjacent word pairs
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))

            # Invalid case: prefix issue (e.g. "abc" before "ab")
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    # Add edge from w1[j] -> w2[j]
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break  # only first difference matters

        # Step 3: Topological Sort using Kahn's Algorithm
        q = deque([c for c in indegree if indegree[c] == 0])
        res = ""
        while q:
            node = q.popleft()
            res += node
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # Step 4: Cycle detection - if not all letters processed
        return res if len(res) == len(indegree) else ""
