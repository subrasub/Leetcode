class Solution:
    def romanToInt(self, s: str) -> int:
        romanNum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        if (len(s) == 1):
            return romanNum.get(s[0])
        
        num = 0
        i=0
        
        while i<len(s):
            one = romanNum.get(s[i])
            if(i+1 < len(s)):
                two = romanNum.get(s[i+1])
                if(one >= two):
                    num += one
                    i+=1
                else: 
                    num+= two-one
                    i+=2
            else:
                num += one
                i+=1
        return num

