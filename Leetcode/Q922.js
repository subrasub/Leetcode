/**
 * @param {number[]} A
 * @return {number[]}
 */
var sortArrayByParityII = function(A) {

    var res=[]    
    var k=0, i=0, j=1

    while(k<A.length){
        if(A[k]%2 === 0){
            res[i]=A[k]
            i+=2
        }
        else{
            res[j] = A[k]
            j+=2
        }   
        k++
    }
    return res
};