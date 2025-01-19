/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    var bin = init
    for(let i = 0; i<nums.length; i++){
        bin = fn(bin,nums[i])
    }
    return bin
};