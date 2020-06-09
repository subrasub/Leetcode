# https://leetcode.com/problems/occurrences-after-bigram/
# Tags - Hash Table

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = text.split()
        ans = []
        
        for i in range(0, len(res)-2):
            if(res[i] == first):
                if(res[i+1] == second):
                    if(i+2 < len(res)):
                        ans.append(res[i+2])
                    
        return ans