# https://leetcode.com/problems/path-sum/
# Tags - Tree, Depth-first Search

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        else:
            if root.left is None and root.right is None and root.val==sum:
                return True
            
            sum -= root.val
            
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)