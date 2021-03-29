# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def countNodes(self, root: TreeNode) -> int:
    def getDepth(node):
      if not node:
        return 0
      return 1+getDepth(node.left)

    if not root:
      return 0
    leftD = getDepth(root.left)
    rightD = getDepth(root.right)

    if leftD == rightD:
      return pow(2, leftD) + self.countNodes(root.right)
    else:
      return pow(2, rightD) + self.countNodes(root.left)
