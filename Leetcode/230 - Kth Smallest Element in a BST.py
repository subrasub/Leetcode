# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(node, arr):
            if not node:
                return arr

            helper(node.left, arr)
            arr.append(node.val)
            helper(node.right, arr)

            return arr

        res = helper(root, [])
        return res[k-1]
