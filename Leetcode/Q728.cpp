#include<iostream>
using namespace std;

class Solution {
public:
    vector<int> selfDividingNumbers(int left, int right) {
        vector<int> res;
        for(int i=left; i<=right; i++){
            if(selfDivision(i))
                res.push_back(i);
        }      
     return res;   
    }
    
    bool selfDivision(int x){
        int copy = x;
        while(copy>0){
            int dig = copy%10;
            if(dig == 0) return false;
            if(x%dig != 0) return false;
            copy = copy/10;
        }
        return true;  
    }
};