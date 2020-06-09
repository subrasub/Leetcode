# https://leetcode.com/problems/two-city-scheduling/
# Tags - Greedy

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        res = 0
        
        # Sort according to the absolute difference of the values
        costs.sort(key = lambda x: x[0]-x[1])
        print(costs)
        
        N = len(costs)//2
        
        for x,y in costs:
            if N > 0:
                res += x
                print(x)
            else:
                res += y
                print(y)   
            N -= 1
             
        return res
