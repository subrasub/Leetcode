# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def closestValue(self, root: TreeNode, target: float) -> int:
    if not root:
      return

    stack = []
    prev = float('-inf')

    while(stack or root):
      while root:
        stack.append(root)
        root = root.left
      root = stack.pop()

      if prev<=target and target<root.val:
        return min(root.val, prev, key = lambda x: abs(target - x))

      prev = root.val
      root = root.right

    return prev