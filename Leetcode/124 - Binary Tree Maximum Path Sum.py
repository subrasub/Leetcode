# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxGain(node):
            nonlocal maxSum
            if not node:
                return 0

            left = max(maxGain(node.left), 0)
            right = max(maxGain(node.right), 0)

            new_path = node.val + left + right

            maxSum = max(new_path, maxSum)
            return node.val + max(left, right)

        maxSum = -math.inf
        maxGain(root)
        return maxSum