# https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = {}
        for word in strs:
            val = ''.join(sorted(list(word)))
            if val not in table: 
                table[val] = [word]
            else:
                table[val].append(word)
        
        return table.values()   