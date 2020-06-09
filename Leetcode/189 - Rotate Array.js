// https://leetcode.com/problems/rotate-array/
// Tags - Array

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var rotate = function(nums, k) {
    //Didn't know you could do this in JS, wow!

    var shift = nums.splice(nums.length-k)
    nums.unshift(... shift)
};
