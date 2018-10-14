/**
 * @param {string} S
 * @return {number}
 */
var minAddToMakeValid = function(S) {
    if(S.length === 0)
        return 0
    
    var stack=[]
    var p=0
    
    for(let i=0; i<S.length; i++){
        if(S[i]==='(')
            stack.push(S[i])
        
        if(S[i] === ')'){
            if(stack.length === 0 || stack[stack.length-1]!='(')
                p++
            else
                stack.pop()
        }
    }
    
    for(var i=0; i<stack.length; i++){
        if(stack[i] === '(')
            p++
    } 
    return p
};