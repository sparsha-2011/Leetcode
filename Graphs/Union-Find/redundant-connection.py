# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/redundant-connection/
# Date: 2025-04-23
# Tags: union-find, disjoint-set, graphs, cycle-detection, DSU

from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Initialize parent and rank arrays for Union-Find
        parent = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  # Compress the path
            return parent[x]

        # Union function with union by rank
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False  # x and y are already connected; adding this edge would create a cycle

            # Attach smaller tree under larger one (union by rank)
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        # Try to union all edges; the one that fails is the redundant connection
        for u, v in edges:
            if not union(u, v):
                return [u, v]
