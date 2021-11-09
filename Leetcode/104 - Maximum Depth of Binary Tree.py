# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.max = 0

        def helper(node, level):
            if not node:
                return 0

            if not node.left and not node.right:
                self.max = max(level, self.max)

            helper(node.left, level+1)
            helper(node.right, level+1)

        helper(root, 1)
        return self.max
