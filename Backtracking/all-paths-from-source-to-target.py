# Date: 2025-05-28
# Author: Sparsha Srinath
# Leetcode: https://leetcode.com/problems/all-paths-from-source-to-target/
# Tags: DFS, Backtracking, Graph
# Problem: 797. All Paths From Source to Target
# Description:
# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
# find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as an adjacency list, where graph[i] is a list of all nodes you can visit from node i.

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        res = []  # to store all valid paths
        
        def dfs(node, path):
            # Base case: if we reached the target node (n - 1)
            if node == len(graph) - 1:
                res.append(path[:])  # make a copy of the path
                return
            
            # Recursive case: visit all the neighbors
            for neighbor in graph[node]:
                path.append(neighbor)       # choose
                dfs(neighbor, path)         # explore
                path.pop()                  # un-choose (backtrack)

        dfs(0, [0])  # start DFS from node 0 with path [0]
        return res
