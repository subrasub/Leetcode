# https://leetcode.com/problems/symmetric-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def mirror(node1, node2):
            if (node1 is None and node2 is None):
                return True
            if (node1 is None or node2 is None):
                return False
            
            return (node1.val == node2.val) and mirror(node1.right, node2.left) and mirror(node1.left, node2.right)
        
        return mirror(root, root)
