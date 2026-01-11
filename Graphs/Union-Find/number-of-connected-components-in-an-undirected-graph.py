# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Date: 2025-04-23
# Tags: union-find, disjoint-set, graphs, connected-components

from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
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
                return False  # Already connected

            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

            return True

        # Union all edges
        for u, v in edges:
            union(u, v)

        # Count unique connected components
        roots = set(find(i) for i in range(n))
        return len(roots)
