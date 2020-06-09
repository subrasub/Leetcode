class Solution {
public:
    int reverse(int x) {
        
        int res=0; 
        while(x!=0){
            int d = x%10;
            // accounting for the integer overflow
            if(res > INT_MAX/10)
                return 0;
            if(res < INT_MIN/10)
                return 0;
            res = 10*res + d;
            x/=10;
        }
        return res;
    }
};