# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def inorderTraversal(self, root: TreeNode) -> List[int]:
    def inorder(node):
      if not node:
        return
      inorder(node.left)
      self.res.append(node.val)
      inorder(node.right)

    self.res = []
    inorder(root)

    return self.res
