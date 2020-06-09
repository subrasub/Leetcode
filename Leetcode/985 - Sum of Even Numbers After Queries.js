// https://leetcode.com/problems/sum-of-even-numbers-after-queries/
// Tags - Array

/**
 * @param {number[]} A
 * @param {number[][]} queries
 * @return {number[]}
 */
var sumEvenAfterQueries = function(A, queries) {
    var res = []
    for(var i=0; i<A.length; i++){
        var val = queries[i][0]
        var index = queries[i][1]
        A[index] += val;
        var sum = 0;
        for(var k=0; k<A.length; k++){
            if(A[k]%2 == 0){
                sum+=A[k];
            }
        }
        res[i] = sum;
    }
    return res
};