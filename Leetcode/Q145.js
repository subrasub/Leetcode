/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var postorderTraversal = function(root){
    if(root === null)
       return []
    
    var res=[]
    var stack = []
    
    stack.push(root)
    while(stack.length !== 0){
        var k = stack.pop()
        res.unshift(k.val)
        
        if(k.left!==null)
            stack.push(k.left)
        if(k.right !== null)
            stack.push(k.right)
    }
    return res
};