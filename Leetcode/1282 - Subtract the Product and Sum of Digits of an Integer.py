class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = 0
        prod = 1
        
        while(n):
            d = n%10
            s+=d
            prod*=d
            n = n//10
        return prod-s