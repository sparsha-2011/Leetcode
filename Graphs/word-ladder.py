# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/word-ladder/
# Date: 2025-04-23
# Tags: bfs, graphs, shortest-path, word-ladder, pattern-matching

from collections import deque, defaultdict
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        # Build adjacency map with intermediate patterns
        nei = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                nei[pattern].append(word)

        q = deque([beginWord])
        visited = set([beginWord])
        steps = 1  # Begin word is counted as step 1

        # BFS to find shortest path
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps

                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in nei[pattern]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            q.append(neighbor)
            steps += 1

        return 0  # No valid transformation sequence found
