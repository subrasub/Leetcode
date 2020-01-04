class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        value = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        res = ""
        # hardcoded i to start from the last element of the roman-value array
        i=12
        
        while(num):
            quotient = num//value[i]
            num = num % value[i]
            
            while(quotient):
                res += roman[i]
                quotient -= 1
            
            i-=1
        
        return res
                
        
