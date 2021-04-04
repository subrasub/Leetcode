# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
      return []

    res = []

    def traverse(node, level):
      if len(res) == level:
        res.append([])

      res[level].append(node.val)

      if node.left:
        traverse(node.left, level+1)
      if node.right:
        traverse(node.right, level+1)

    traverse(root, 0)
    return res