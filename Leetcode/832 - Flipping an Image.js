// https://leetcode.com/problems/flipping-an-image/
// Tags - Array

/**
 * @param {number[][]} A
 * @return {number[][]}
 */
var flipAndInvertImage = function(A) {
    for(var i=0; i<A[0].length; i++)
        A[i] = A[i].reverse()
    
    for(var i=0; i<A[0].length; i++)
        for(var k=0; k<A.length; k++){
            if(A[i][k] === 0)
                A[i][k] = 1
            else
                A[i][k] = 0
        }
    return A
};