/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    
    k%=nums.length
    
    function r_inplace(nums, l, r){
        while(l<=r){
            var temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            l++
            r--
        }
        return nums
    }
    r_inplace(nums, 0, nums.length-1)
    r_inplace(nums, 0, k-1)
    r_inplace(nums, k , nums.length-1)
};
