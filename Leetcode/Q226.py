# https://leetcode.com/problems/invert-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is None: 
            return 
        else:
            self.invertTree(root.left)
            self.invertTree(root.right)
            
            temp = root.left
            root.left = root.right
            root.right = temp
            
        return root
