# Author: Sparsha Srinath
# Date: 2025-11-09
# Problem: Find the Town Judge
# Link: https://leetcode.com/problems/find-the-town-judge/
# Tags: Graph, In-degree / Out-degree, Array
# Time Complexity: O(N + T)  where T = len(trust)
# Space Complexity: O(N)

from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        # indegree[i]  = number of people who trust person i+1
        # outdegree[i] = number of people person i+1 trusts
        indegree = [0] * n
        outdegree = [0] * n

        # Populate indegree and outdegree arrays
        for u, v in trust:
            indegree[v - 1] += 1
            outdegree[u - 1] += 1
        
        # The town judge:
        # 1. Trusts nobody -> outdegree == 0
        # 2. Is trusted by everyone else -> indegree == n - 1
        for i in range(n):
            if outdegree[i] == 0 and indegree[i] == n - 1:
                return i + 1
        
        # If no such person exists, return -1
        return -1
