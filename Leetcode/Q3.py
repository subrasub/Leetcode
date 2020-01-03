class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        keys = set()
        i = 0
        j = 0
        maxCount = 0
        
        while(i<len(s) and j<len(s)):
            if(s[j] not in keys):
                keys.add(s[j])
                j += 1
                maxCount = max(maxCount, j-i)
            else:
                keys.remove(s[i])
                i+=1
        
        return maxCount