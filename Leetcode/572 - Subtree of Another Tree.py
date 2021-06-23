# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def match(s, t):
            if not(s and t):
                return s is t

            return (s.val == t.val and
                    match(s.left, t.left) and
                    match(s.right, t.right))

        if match(root, subRoot):
            return True

        if not root:
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
