// https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/
// Tags - Binary Search Tree

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int sum = 0;
    TreeNode* bstToGst(TreeNode* root) {
        if(root == NULL)
            return NULL;
        
        bstToGst(root->right);
        root->val = sum +=root->val;
        bstToGst(root->left);
        
        return root;
    }
};