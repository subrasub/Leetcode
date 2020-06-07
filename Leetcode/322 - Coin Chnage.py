# https://leetcode.com/problems/coin-change/
# Tags - Dynamic Programming

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = (amount+1)*[float('inf')]
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount+1):
                dp[x] = min(dp[x], dp[x-coin]+1)
        
        if dp[amount] != float('inf'):
            return dp[amount]
        else:
            return -1
