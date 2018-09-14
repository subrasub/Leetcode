class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> r(2,0);
        for(int i=0; i<nums.size(); i++){
            for(int j=i+1; j<nums.size(); j++){
                if((nums[i]+nums[j])==target){
                    r[0] = i;
                    r[1] = j;
                }
                    
            }
        }
        return r;
    }
};