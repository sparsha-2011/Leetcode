# Author: Sparsha Srinath
# URL: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
# Date: 2026-05-25
# Tags: graph, dfs, connected-components, adjacency-list
# Description:
#   Given n nodes and a list of undirected edges, find the number of connected
#   components. Build an adjacency list (both directions for undirected), then
#   DFS from each unvisited node. Each new DFS call from the main loop discovers
#   a new component.
#
#   DFS Pattern 1 — Component Finding:
#     for every node:
#         if not visited → start DFS → that's one component
#
#   Key: adjacency list must add BOTH directions for undirected graphs.
#   Without both, DFS misses connections and overcounts components.
#
# Input: n (int), edges (List[List[int]])
# Output: int — number of connected components
#
# Example:
#   Input : n=5, edges=[[0,1],[1,2],[3,4]]
#   Output: 2 (components: {0,1,2} and {3,4})
#
# Time Complexity : O(V + E) where V = nodes, E = edges
# Space Complexity: O(V + E) for adjacency list and visited set

from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjL = defaultdict(list)
        for u, v in edges:
            adjL[u].append(v)
            adjL[v].append(u)

        components = 0
        visit = set()

        def dfs(node):
            visit.add(node)
            for nei in adjL[node]:
                if nei not in visit:
                    dfs(nei)

        for i in range(n):
            if i not in visit:
                dfs(i)
                components += 1

        return components


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
