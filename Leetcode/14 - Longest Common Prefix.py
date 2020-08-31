# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not len(strs):
            return ""
        
        prefix = strs[0]
        
        for i in range(len(prefix)):
            for word in strs[1:]:
                if i>=len(word) or word[i] != prefix[i]:
                    return prefix[:i]
        return prefix