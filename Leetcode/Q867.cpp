class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& A) {
        vector<vector<int>> res(A[0].size(), vector<int>(A.size()));
        
        for(int r=0; r<A.size(); r++){
            for(int c=0; c<A[0].size(); c++){
                res[c][r] = A[r][c];
            }
        }
        return res;
    }
};