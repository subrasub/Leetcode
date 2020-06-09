# https://leetcode.com/problems/queue-reconstruction-by-height/
# Tags - Greedy

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for x,y in people:
            res.insert(y, (x,y))
        
        return res
