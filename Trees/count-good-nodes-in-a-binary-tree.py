# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        Returns the number of good nodes in the binary tree.
        
        A good node is a node whose value is greater than or equal to 
        the maximum value encountered from the root to that node along 
        the path.

        This solution uses Depth-First Search (DFS) to traverse the tree 
        and count the good nodes.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree, due to 
        the recursion stack used in DFS.
        """

        def dfs(node, maxVal):
            """
            Helper function to perform DFS and count good nodes.
            
            Args:
                node (TreeNode): The current node in the tree.
                maxVal (int): The maximum value encountered along the path 
                              from the root to the current node.
                              
            Returns:
                int: The number of good nodes in the subtree rooted at the current node.
            """
            if not node:
                return 0

            # Count the current node as good if its value is greater than or equal to maxVal
            res = 1 if node.val >= maxVal else 0
            
            # Update the maxVal for the next recursive calls
            maxVal = max(maxVal, node.val)

            # Recursively count good nodes in the left and right subtrees
            res += dfs(node.left, maxVal)
            res += dfs(node.right, maxVal)

            return res
        
        # Start the DFS with the root node and its value as the initial maxVal
        return dfs(root, root.val)
