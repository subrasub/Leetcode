# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Tags - Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        left = {}
        
        def searchDFS(node, depth = 0, position = 0):
            if node:
                left.setdefault(depth, position)
                self.ans = max(self.ans, position-left[depth]+1)
                searchDFS(node.left, depth+1, position*2)
                searchDFS(node.right, depth+1, position*2+1)
        
        searchDFS(root)
        return self.ans
                
