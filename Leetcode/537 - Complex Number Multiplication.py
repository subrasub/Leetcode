# https://leetcode.com/problems/complex-number-multiplication/
# Tags - Math, String

class Solution:
    def complexNumberMultiply(self, a: str, b: str) -> str:
        num1 = a.replace('i','').split('+')
        num2 = b.replace('i','').split('+')
        res = ['x', 'x']
        
        print(num1, num2)
        
        res[0] = int(num1[0])*int(num2[0]) - int(num1[1])*int(num2[1]) 
        res[1] = int(num1[0])*int(num2[1]) + int(num1[1])*int(num2[0]) 
        
        return str(res[0]) + "+" + str(res[1]) + "i"
