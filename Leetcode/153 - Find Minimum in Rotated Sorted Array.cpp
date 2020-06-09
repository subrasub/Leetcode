// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
// Tags - Array, Binary Search

class Solution {
public:
    int findMin(vector<int>& nums) {
        cout<<nums.size();
        if(nums.size()==1)
            return nums[0];
        else{
             for(int i=0; i<nums.size(); i++){
                if(nums[0] < nums[nums.size()-1])
                    return nums[0];

                if(nums[i+1]<nums[i])
                    return nums[i+1];
            }
        }
        return 0;
    }
};