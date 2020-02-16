class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=="0":
            return 0
        
        count = [0]*(len(s)+1)
        
        count[0], count[1] = 1,1
        
        for i in range(2, len(s)+1):
            count[i] = 0
            
            if(s[i-1] > '0'):
                count[i] = count[i-1]
            
            if(s[i-2] == '1' or (s[i-2] == '2' and s[i-1]<'7')):
                count[i] += count[i-2]
        
        return count[-1]
        
