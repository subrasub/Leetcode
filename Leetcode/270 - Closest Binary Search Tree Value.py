# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def closestValue(self, root: TreeNode, target: float) -> int:
    def dfs(node):
      if not node:
        return
      if (abs(target-node.val) < self.minGap):
        self.minGap = abs(target-node.val)
        self.res = node.val
      dfs(node.left)
      dfs(node.right)

    self.minGap = float('inf')
    self.res = 0
    dfs(root)

    return self.res