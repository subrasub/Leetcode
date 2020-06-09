# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/
# Tags - String

class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = ""
        alphabet = collections.defaultdict(str)
        
        # string.ascii_lowercase return list of all alphabets in lowercase
        for index, letter in enumerate(string.ascii_lowercase):
            alphabet[str(index+1)] = letter
        
        i = 0
        while i<len(s):
            if i+2 < len(s) and s[i+2]=='#':
                res += alphabet[s[i:i+2]]
                i += 3
            else:
                res += alphabet[s[i]]
                i += 1
                
        return res
                
            
                
                
