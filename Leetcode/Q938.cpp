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
    int sum;
    int rangeSumBST(TreeNode* root, int L, int R) {
        sum = 0;
        helper(root, L, R);
        return sum;
    }
    
    void helper(TreeNode* root, int L, int R){
        
        if(root != nullptr){
            if(L<= root->val && R>=root->val)
                sum+=root->val;

            if(L<root->val)
                helper(root->left, L, R);

            if(R>root->val)
                helper(root->right, L, R);
        } 
    }
};