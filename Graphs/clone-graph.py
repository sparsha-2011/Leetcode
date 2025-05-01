
# Author: Sparsha Srinath
# Date: 2025-04-30
# URL: https://leetcode.com/problems/clone-graph/
# Tags: graph, dfs, hashmap, clone

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Dictionary to store mapping from original node to its clone
        oldToNew = {}

        def dfs(node):
            # If already cloned, return the clone
            if node in oldToNew:
                return oldToNew[node]

            # Clone the current node
            new_node = Node(node.val)
            oldToNew[node] = new_node

            # Recursively clone all neighbors
            for nei in node.neighbors:
                new_node.neighbors.append(dfs(nei))
            return new_node

        # Handle empty input graph
        return dfs(node) if node else None
