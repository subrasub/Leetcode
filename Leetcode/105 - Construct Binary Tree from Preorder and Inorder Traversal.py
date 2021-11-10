# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(preorder, inorder):
            if not inorder:
                return None

            rval = preorder[0]
            root = TreeNode(rval)

            index_inorder = self.table[rval]

            left_inorder = inorder[:index_inorder]
            right_inorder = inorder[index_inorder+1:]

            left_preorder = preorder[1 : len(left_inorder)+1]
            right_preorder = preorder[len(left_inorder)+1:]

            root.left = self.buildTree(left_preorder, left_inorder)
            root.right = self.buildTree(right_preorder, right_inorder)

            return root

        self.table = {}
        for index, val in enumerate(inorder):
            self.table[val] = index

        return helper(preorder, inorder)