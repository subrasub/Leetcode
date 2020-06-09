# https://leetcode.com/problems/first-unique-character-in-a-string/
# Tags - Hash Table, String

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = collections.Counter(s)
        print(count)
        
        for index, ch in enumerate(s):
            if count[ch] == 1:
                return index
        return -1
