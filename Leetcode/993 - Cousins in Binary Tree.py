# https://leetcode.com/problems/cousins-in-binary-tree/
# Tags - Tree, Breadth-first Search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        def dfs(root, parent, depth):
            if root:
                if root.val == x or root.val == y:
                    res.append((parent, depth))
                
                dfs(root.left, root, depth+1)
                dfs(root.right, root, depth+1)
        
        res = []
        dfs(root, None, 0)
        
        if res[0][0]!=res[1][0] and res[0][1]==res[1][1]:
            return True
        else:
            return False
