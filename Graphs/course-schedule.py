# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/course-schedule/
# Date: 2025-04-23
# Tags: topological-sort, graphs, BFS, Kahn-algorithm, cycle-detection

from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Initialize adjacency list for each course
        adj = {i: [] for i in range(numCourses)}
        # Initialize indegree array to count number of prerequisites for each course
        indegree = [0] * numCourses
        
        # Build the graph: for each course, track its prerequisites
        for crs, preq in prerequisites:
            adj[crs].append(preq)
            indegree[preq] += 1
        
        # Queue for BFS: start with nodes that have zero indegree (no prerequisites)
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # Count of courses that can be finished
        finish = 0
        
        # Process the graph using BFS
        while q:
            node = q.popleft()
            finish += 1  # Course can be finished
            # Reduce indegree of neighboring nodes (prerequisites of this course)
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                # If indegree becomes 0, it means all its prerequisites are met
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        
        # If finish count matches numCourses, all courses can be finished
        return finish == numCourses
