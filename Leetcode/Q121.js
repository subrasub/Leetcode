/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if(prices.length < 2)
        return 0
    
    var minp = prices[0]
    var maxp = prices[1]-prices[0]
    
    for(let i=1; i<prices.length; i++){
        var possible_profit = prices[i]-minp
        maxp = Math.max(maxp, possible_profit)
        minp = Math.min(minp, prices[i])
    }
    return (maxp>0? maxp: 0)
};