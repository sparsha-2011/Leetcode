from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leftSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Returns the values of the nodes visible from the left side of the binary tree.

        This implementation uses Breadth-First Search (BFS) and captures
        the first node (leftmost) at each level.

        Time Complexity: O(n) where n is the number of nodes
        Space Complexity: O(n) for queue and result list
        """

        # BFS implementation
        res = []
        q = deque([root])

        while q:
            leftNode = None  # Keeps track of the leftmost node at the current level
            qLen = len(q)

            for _ in range(qLen):
                node = q.popleft()
                if node:
                    if leftNode is None:
                        leftNode = node  # The first node processed at this level is the leftmost
                    q.append(node.left)
                    q.append(node.right)
            
            if leftNode:
                res.append(leftNode.val)

        # Optional DFS version:
        # def dfs(node, level):
        #     if not node:
        #         return
        #     if level == len(res):
        #         res.append(node.val)  # Capture the first node at each level
        #     dfs(node.left, level + 1)  # Explore left child first (to prioritize left side)
        #     dfs(node.right, level + 1)

        # dfs(root, 0)

        return res
