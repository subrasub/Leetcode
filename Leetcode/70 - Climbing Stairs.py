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
    class Solution:
    def climbStairs(self, n: int) -> int:
        def climbFind(i, n):
            if i > n:
                return 0
            if i == n:
                return 1
            if self.dp[i] > 0:
                return self.dp[i]

            self.dp[i] = climbFind(i+1, n) + climbFind(i+2, n)
            return self.dp[i]

        self.dp = [0 for _ in range(n+1)]
        return climbFind(0, n)
