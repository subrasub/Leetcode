# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: 
            return 0
        
        def dfs(node, res):
            if not node:
                return 0
            if node:
                res = res*10 + node.val
                
                if(node.right is None and node.left is None):
                    return res
                
                return (dfs(node.left, res) + dfs(node.right, res))
        
        return dfs(root, 0)
