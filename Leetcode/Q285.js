/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {TreeNode} p
 * @return {TreeNode}
 */
var inorderSuccessor = function(root, p) {
    var next = null
    while(root != null){
        if(p.val<root.val){
            next = root
            root = root.left
        }
        else
            root = root.right
    }
    return next
};