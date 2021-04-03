# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def bstToGst(self, root: TreeNode) -> TreeNode:
    def traverse(node):
      if not node:
        return

      traverse(node.right)

      self.res += node.val
      node.val = self.res

      traverse(node.left)

    self.res = 0
    traverse(root)

    return root
