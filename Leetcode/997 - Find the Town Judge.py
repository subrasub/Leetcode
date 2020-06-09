# https://leetcode.com/problems/find-the-town-judge/
# Tags - Graph

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        table = [0]*(N+1)
        
        for x,y in trust: 
            table[x] -= 1
            table[y] += 1
        
        for i in range(1, N+1):
            if table[i] == N-1:
                return i
        return -1
