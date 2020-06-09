// https://leetcode.com/problems/squares-of-a-sorted-array/
// Tags - Array, Two Pointers

/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortedSquares = function(A) {
    for(var i=0; i<A.length; i++){
        A[i] = A[i]*A[i];
    }
    console.log(A)
    return A.sort(function (a,b){ return a-b;})
};