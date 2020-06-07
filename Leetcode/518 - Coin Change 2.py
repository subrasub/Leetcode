# https://leetcode.com/problems/coin-change-2/
# Tags - Dynamic Programming

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = (amount+1)* [0]
        dp[0] = 1
        
        for coin in coins:
            for x in range(1, amount+1):
                if x >= coin:
                    dp[x] += dp[x-coin]
        
        return dp[amount]