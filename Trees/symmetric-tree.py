# LeetCode Problem: Symmetric Tree
# Link: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        Determines if a binary tree is symmetric around its center.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(h), where h is the height of the tree due to recursion stack.

        :type root: TreeNode
        :rtype: bool
        """
        
        def isMirror(left, right):
            """
            Helper function to check if two trees are mirror images of each other.

            :type left: TreeNode
            :type right: TreeNode
            :rtype: bool
            """
            # Base cases:
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            # Check if current nodes are equal and recurse for children
            return (left.val == right.val and
                    isMirror(left.left, right.right) and
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right)
