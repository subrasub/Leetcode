# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies
# Tags - Array

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        res = []
        
        for i in candies:
            if i+extraCandies >= m:
                res.append(True)
            else:
                res.append(False)
        return res
