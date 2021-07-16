# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        table = defaultdict(list)
        minC = maxC = 0
        queue = deque([(root, 0)])

        while queue:
            node, col = queue.popleft()

            if node:
                table[col].append(node.val)
                minC = min(minC, col)
                maxC = max(maxC, col)

                queue.append((node.left, col-1))
                queue.append((node.right, col+1))

        return [table[val] for val in range(minC, maxC+1)]