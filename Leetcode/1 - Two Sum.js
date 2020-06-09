/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var mymap = {}
    
    for(let i=0; i<nums.length; i++){
    
        var comp = target - nums[i]
        
        if(mymap[comp] !== undefined)
            return [mymap[comp], i]
        
        else
            mymap[nums[i]] = i 
    }
    return 0
};