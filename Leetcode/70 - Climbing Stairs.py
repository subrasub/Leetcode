# https://leetcode.com/problems/climbing-stairs
# Tags - Dynamic Programming

class Solution:
    # iterative way
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        
        dp = [0]*(n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
        
    # recursive way
    def climbStairs(self, n: int) -> int:
        def helper(i, n, memo):
            if i>n:
                return 0
            
            if i==n:
                return 1
            
            if memo[i]:
                return memo[i]

            memo[i] = helper(i+1, n, memo) + helper(i+2, n, memo)
            return memo[i]

        memo = [0]*n
        return helper(0, n, memo)
    