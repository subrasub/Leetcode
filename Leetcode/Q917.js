/**
 * @param {string} S
 * @return {string}
 */

var isAlpha = function(ch){
  return /^[A-Z]$/i.test(ch);
}

var reverseOnlyLetters = function(S) {
    var stack = []
    var res=""
    for(var i=0; i<S.length; i++){
        if(isAlpha(S[i]))
            stack.push(S[i])
    }
    
    for(var i=0; i<S.length; i++){
        if(isAlpha(S[i])){
            var k = stack.pop()
            res += k
        }
        else
            res += S[i]
    }
    return res
};