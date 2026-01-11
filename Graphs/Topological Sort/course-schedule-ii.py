# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/course-schedule-ii/
# Date: 2025-04-23
# Tags: topological-sort, graphs, BFS, Kahn-algorithm, course-scheduling

from collections import deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize adjacency list for each course
        adj = {i: [] for i in range(numCourses)}
        # List to store the result (topological order)
        result = []
        # Array to track number of prerequisites for each course
        indegree = [0] * numCourses
        
        # Build the graph: course -> prerequisites
        for crs, preq in prerequisites:
            adj[crs].append(preq)
            indegree[preq] += 1
        
        # Initialize the queue with courses that have no prerequisites
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        # Counter to track how many courses have been processed
        finish = 0
        
        # Perform BFS (Kahn's Algorithm)
        while q:
            node = q.popleft()
            finish += 1
            result.append(node)  # Append to result in reverse topological order
            # Decrease indegree of each prerequisite of current course
            for neighbour in adj[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    q.append(neighbour)
        
        # If all courses are processed, return the reverse of the result
        return result[::-1] if finish == numCourses else []
