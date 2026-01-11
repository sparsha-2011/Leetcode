# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/graph-valid-tree/
# Date: 2025-04-23
# Tags: union-find, disjoint-set, graphs, cycle-detection, connected-components

from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Initialize parent and rank arrays for Union-Find
        parent = [i for i in range(n)]
        rank = [0] * n

        # Find function with path compression
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Union function with union by rank
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if root_x == root_y:
                return False  # Cycle detected

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        # A valid tree must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Union all edges and check for cycles
        for u, v in edges:
            if not union(u, v):
                return False

        # Finally, check if the graph is fully connected
        roots = set(find(i) for i in range(n))
        return len(roots) == 1
