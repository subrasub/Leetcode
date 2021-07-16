# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for word in strs:
            table[tuple(sorted(word))].append(word)

        return table.values()