# LeetCode Problem: Serialize and Deserialize N-ary Tree
# Link: https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children if children is not None else []

class Codec:
    def serialize(self, root: 'Node') -> str:
        """
        Encodes an N-ary tree to a single string.

        Time Complexity: O(n), where n is the number of nodes in the tree.
        Space Complexity: O(n) for the string and recursion stack.

        :type root: Node
        :rtype: str
        """
        res = []

        def dfs(node):
            if not node:
                return
            res.append(str(node.val))
            res.append(str(len(node.children)))  # Number of children
            for child in node.children:
                dfs(child)
        
        dfs(root)
        return ','.join(res)
    
    def deserialize(self, data: str) -> 'Node':
        """
        Decodes your encoded data to tree.

        Time Complexity: O(n), where n is the number of nodes.
        Space Complexity: O(n), for the recursion stack and internal data structure.

        :type data: str
        :rtype: Node
        """
        vals = data.split(',')
        self.index = 0

        def dfs():
            if self.index >= len(vals):
                return None
            
            val = int(vals[self.index])
            self.index += 1
            num_children = int(vals[self.index])
            self.index += 1

            node = Node(val)
            children = []
            for _ in range(num_children):
                children.append(dfs())
            
            node.children = children
            return node
        
        return dfs()

# Example usage:
# ser = Codec()
# deser = Codec()
# tree = deser.deserialize(ser.serialize(root))
