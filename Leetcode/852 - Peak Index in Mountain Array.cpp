class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) {
        
        for(int i=1; i<A.size(); i++){
            if(A[i-1]>A[i])
                return i-1;
        }
    }
};