// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
// Tags - Array, Greedy

/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if(prices.length < 2)
        return 0
    
    let profit = 0
    let i=1
    
    while(i<prices.length){
        if(prices[i]>prices[i-1]){
            profit+=prices[i]-prices[i-1]  
        }       
        i++
    }
    return profit
};