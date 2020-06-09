// https://leetcode.com/problems/hamming-distance/
// Tags - Bit Manipulation

class Solution {
public:
    int hammingDistance(int x, int y) {
  
        int count = 0;
        int bin = x^y;
        while(bin){
            if(bin&1)
                count++;
            bin = bin>>1;
        }
    return count;       
    }
};