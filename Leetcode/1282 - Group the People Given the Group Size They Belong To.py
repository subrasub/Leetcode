# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# Tags - Greedy

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        tempRes = collections.defaultdict(list)
        res = []
        
        for index, val in enumerate(groupSizes):
            tempRes[val].append(index)
            if len(tempRes[val])==val:
                res.append(tempRes.pop(val))
                
        return res
