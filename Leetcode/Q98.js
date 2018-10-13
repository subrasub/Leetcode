/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    return helper(root, -Infinity, Infinity);
};


function helper(node, minval, maxval){
    if(node === null)
        return true
    
    if(node.val <= minval || node.val >= maxval)
        return false
    
    const isLeft = helper(node.left, minval, node.val)
    const isRight = helper(node.right, node.val, maxval)
    
    return isRight && isLeft
    
}