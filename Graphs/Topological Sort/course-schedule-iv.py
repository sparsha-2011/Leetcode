# Author: Sparsha Srinath
# Date: 2025-11-09
# Problem: Course Schedule IV
# Link: https://leetcode.com/problems/course-schedule-iv/
# Tags: Graph, Topological Sort, BFS, DAG
# Time Complexity: O(N + P + Q) 
#   where N = numCourses, P = len(prerequisites), Q = len(queries)
# Space Complexity: O(N^2) in worst case due to prerequisite sets

from typing import List
from collections import defaultdict, deque

class Solution:
    def checkIfPrerequisite(
        self,
        numCourses: int,
        prerequisites: List[List[int]],
        queries: List[List[int]]
    ) -> List[bool]:
        
        # Build adjacency list and indegree array
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        # prereqSet[i] will store all prerequisites of course i
        prereqSet = [set() for _ in range(numCourses)]

        # Initialize queue with courses having no prerequisites
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # Topological sort (Kahn's Algorithm)
        while q:
            node = q.popleft()
            for nei in graph[node]:
                # Add current node as a prerequisite
                prereqSet[nei].add(node)
                # Also inherit all prerequisites of the current node
                prereqSet[nei].update(prereqSet[node])

                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        
        # Answer queries: check if u is a prerequisite of v
        return [u in prereqSet[v] for u, v in queries]
