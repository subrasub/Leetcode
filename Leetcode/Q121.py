class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        maxP = 0
        minP = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < minP:
                minP = prices[i]
            tempMax = prices[i] - minP
            if(tempMax > maxP):
                maxP = tempMax
                
        return maxP
            
