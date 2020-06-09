# https://leetcode.com/problems/univalued-binary-tree/
# Tags - Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root == None:
            return 
        res=[]
        def dfs(node):
            if node:
                res.append(node.val)
                dfs(node.left)
                dfs(node.right)
        
        dfs(root)
        return len(set(res)) == 1